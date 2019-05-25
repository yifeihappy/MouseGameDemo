import threading
import pickle
from Controller import *
import time
import wx


class RecognizerThread(threading.Thread):
    def __init__(self, dq, frame):
        threading.Thread.__init__(self)
        self.dataQueue = dq
        f = open('svm.model', 'rb')
        s = f.read()
        self.classify = pickle.loads(s)
        print("load SVM classfier successfully!")
        self.exitFlag = False
        self.mag_win = []
        self.linear_acc_win = []
        self.recorderData = []
        self.tap_flag = False
        self.frame = frame

    def run(self):
        while not self.exitFlag:
            data_list = []
            while not self.dataQueue.empty():
                listItem = self.dataQueue.get()
                data_list.append(listItem)
                # print(listItem)
            self.keystroke_localization(data_list)
            time.sleep(0.1)
        print("RecognizerThread exit...")
        Controller.write_file(self.recorderData, "recognizeData.txt")

    def keystroke_localization(self, data_list):
        data = np.array(data_list)
        data_len = len(data)
        index = 0
        input_flag = False  # 标记手是否水平放置状态
        while index < data_len:
            self.recorderData.append(data[index, :])
            if 9 == data[index, 0]:
                if np.abs(data[index, 4]) > 7:  # 判断手是否水平放置，阈值设置为8.5
                    input_flag = True
                else:
                    input_flag = False
                    self.mag_win = []
                    self.linear_acc_win = []
            elif input_flag:
                if 10 == data[index, 0]:
                    self.linear_acc_win.append(data[index, :])
                    # 数据量达到一个窗口量
                    if self.linear_acc_win[-1][1] - self.linear_acc_win[0][1] > Controller.acc_time:
                        # 如果刚发生tap事件，则在tap_time时间内不做判断,即，等待对magnetic数据收集完后再进行判断
                        if not self.tap_flag:
                            # 通过能量判断是否达到一个阈值
                            self.tap_flag = Controller.is_tap(self.linear_acc_win, Controller.lacce_thre)
                            # print("is tap?")
                        else:
                            print("wait for magnetic")
                        # 窗口向前滑动，删除旧数据
                        Controller.slide_win(self.linear_acc_win, 0.5, Controller.acc_time)
                elif 2 == data[index, 0]:
                    self.mag_win.append(data[index, :])
                    if self.tap_flag:
                        print("tapping, mag_win_size = " + str(len(self.mag_win)))
                        self.tap_flag = Controller.is_false_stroke(self.mag_win)
                        if self.mag_win[-1][1] - self.mag_win[0][1] > 2 * Controller.mag_time:
                            print("recognize_keystroke")
                            if not self.__localization(self.mag_win.copy()):
                                print("Not a real stroke")
                            self.tap_flag = False
                            # 发生点击事件，并且判断完成后，数据维持在一个mag_time时间大小
                            Controller.slide_win(self.mag_win, 0.1, Controller.mag_time)
                        else:
                            print("T:" + str(self.mag_win[-1][1] - self.mag_win[0][1]))
                    else:
                        # 如果没有发生点击事件，窗口数据量维持在一个mag_time时间大小
                        Controller.slide_win(self.mag_win, 1.0, Controller.mag_time)
            index += 1

    # 收集magnetic数据
    def __localization(self, data):
        np_d = np.array(data)
        dis = abs(np_d[0, 2] - np_d[-1, 2]) + abs(np_d[0, 3] - np_d[-1, 3]) + abs(np_d[0, 4] - np_d[-1, 4])
        f_m = np.sum(np.abs((np_d[0, [2, 3, 4]] + np_d[-1, [2, 3, 4]]) / 2 - np_d[int(np_d.shape[0] / 2), [2, 3, 4]]))
        # 去除抬手情况
        if f_m < Controller.f_stroke_thre_m:
            print('false stroke{ f_m: %f}' % f_m)
            return False
        # 去除传感器受突变的情况
        if dis < Controller.magnetic_thre:
            f = self.__extract_feature(data)
            label = int(self.classify.predict(f.reshape(1, -1)))
            print("Keystroke:%d" % label)
            # btn = self.frame.m_bpButton_list[int(label) - 1]
            # btn.ProcessEvent(wx.CommandEvent(wx.EVT_BUTTON.typeId, btn.GetId()))
            if self.frame.button_id == label:
                self.frame.add_right()
                self.frame.change_button_image(self.frame.button_id, self.frame.image_hit)
            else:
                self.frame.add_error()
            self.frame.change_digit(str(label))
        else:
            print('bad stroke{ dis: %f}' % dis)
        return True

    # 获取数据特征，并打上标签
    def __extract_feature(self, data):
        np_d = np.array(data)
        # 将x,y,z的数据都移到一0开始的位置
        start_data = np_d[-1, :]
        np_d = np_d - start_data
        # 生成x-y,x-z,y-z的数据
        x_np_d = np.c_[np_d[:, 2] - np_d[:, 3], np_d[:, 2] - np_d[:, 4], np_d[:, 3] - np_d[:, 4]]
        xyz = np_d[:, 2:5]
        e_norm = np.sqrt(np.sum(np.square(xyz), axis=1))
        f = np.r_[xyz.max(axis=0), xyz.min(axis=0), xyz.mean(axis=0), np.median(xyz, axis=0),
                  x_np_d.max(axis=0), x_np_d.min(axis=0), x_np_d.mean(axis=0), np.median(x_np_d, axis=0),
                  e_norm.max(), e_norm.min(), e_norm.mean(), np.median(e_norm)]
        return f


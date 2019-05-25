import numpy as np
from sklearn import svm
import pickle
from Controller import *


class ISSDataController:
    def __init__(self, frame):
        # iss
        self.dataArray = []
        self.lastStr = ""
        self.features = []
        # real time keystroke localization
        self.classify = ""
        self.frame = frame

    # decode the data from the smartwatch
    def decode_str(self, data_str):
        data_str = self.lastStr + data_str
        data_str_a = data_str.split("\n")
        is_end = False
        if len(data_str_a) == 1:  # maybe the str is not complete
            self.lastStr = data_str
            if 'E' == data_str[0]:
                is_end = True
        else:
            for i in range(len(data_str_a)-1):
                str_a = data_str_a[i].split(",")
                item_a = list(map(eval, str_a[1:]))  # ignore the first cell "S" or "E"
                self.dataArray.append(item_a)
                if 'E' == str_a[0]:
                    is_end = True
            # keep the last str item
            self.lastStr = data_str_a[-1]
        return is_end

    # 收集magnetic数据
    def segmentation(self, data, label=0):
        np_d = np.array(data)
        dis = abs(np_d[0, 2] - np_d[-1, 2]) + abs(np_d[0, 3] - np_d[-1, 3]) + abs(np_d[0, 4] - np_d[-1, 4])
        f_m = np.sum(np.abs((np_d[0, [2, 3, 4]] + np_d[-1, [2, 3, 4]]) / 2 - np_d[int(np_d.shape[0] / 2), [2, 3, 4]]))
        print('f_m:', f_m)
        # 去除抬手情况
        if f_m < Controller.f_stroke_thre_m:
            print('magnetic change is too small{ f_m: %f}' % f_m)
            return False
        # 去除传感器受突变的情况
        if dis < Controller.magnetic_thre:
            self.extract_feature_label(data, label)
        else:
            print('bad stroke, burst{ dis: %f}' % dis)
        return True

    # 获取数据特征，并打上标签
    def extract_feature_label(self, data, label):
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
                  e_norm.max(), e_norm.min(), e_norm.mean(), np.median(e_norm), label]
        self.features.append(f)

    def get_features_iss(self):
        data = np.array(self.dataArray)
        data_len = len(data)
        index = 0
        label = 0
        input_flag = False  # 标记手是否水平放置状态
        tap_flag = False  # 标记是否发生tap事件
        magnetic_win = []
        linear_accelerometer_win = []
        while index < data_len:
            if 9 == data[index, 0]:
                if np.abs(data[index, 4]) > 7:    # 判断手是否水平放置，阈值设置为8.5
                    input_flag = True
                else:
                    input_flag = False
                    magnetic_win = []
                    linear_accelerometer_win = []
            elif input_flag:
                if 10 == data[index, 0]:
                    linear_accelerometer_win.append(data[index, :])
                    # 数据量达到一个窗口量
                    if linear_accelerometer_win[-1][1] - linear_accelerometer_win[0][1] > Controller.acc_time:
                        # 如果刚发生tap事件，则在tap_time时间内不做判断,即，等待对magnetic数据收集完后再进行判断
                        if not tap_flag:
                            # 通过能量判断是否达到一个阈值
                            tap_flag = Controller.is_tap(linear_accelerometer_win, Controller.lacce_thre)
                        else:
                            print("wait for magnetic")
                        # 窗口向前滑动，删除旧数据
                        Controller.slide_win(linear_accelerometer_win, 0.5, Controller.acc_time)
                elif 2 == data[index, 0]:
                    magnetic_win.append(data[index, :])
                    if tap_flag:
                        tap_flag = Controller.is_false_stroke(magnetic_win)
                        if magnetic_win[-1][1] - magnetic_win[0][1] > 2 * Controller.mag_time:
                            if self.segmentation(magnetic_win.copy(), label):
                                label += 1
                            tap_flag = False
                            # 发生点击事件，并且判断完成后，数据维持在一个mag_time时间大小
                            Controller.slide_win(magnetic_win, 0.1, Controller.mag_time)
                    else:
                        # 如果没有发生点击事件，窗口数据量维持在一个mag_time时间大小
                        Controller.slide_win(magnetic_win, 1.0, Controller.mag_time)
            index += 1

    def train_model_iss(self):
        self.get_features_iss()
        features = np.array(self.features)
        self.classify = svm.SVC(C=0.9, kernel='linear', decision_function_shape='ovo').fit(features[:, 0:-1],
                                                                                           features[:, -1])
        print('Train: accuracy=%f ' % (self.classify.score(features[:, 0:-1], features[:, -1])))  # 精度
        # save model
        mp = pickle.dumps(self.classify)
        f = open('svm.model', "wb+")
        f.write(mp)
        f.close()
        print("Save model successfully!")
        print("Class Num:%d" % (features[-1, -1]+1))
        self.frame.m_staticText_Key_num_value.SetLabel(str(features[-1, -1] + 1))
        Controller.write_file(features, 'features.txt')
        Controller.write_file(self.dataArray, "iss.txt")




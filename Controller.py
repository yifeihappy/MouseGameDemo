import numpy as np


class Controller:
    acc_time = 30
    mag_time = 400  # keystroke localization 需要magnetic数据的时间窗口为[t-win_time, t+win_time]，所以要保留前win_time的data 400
    lacce_thre = 1  # 判断是否有stroke事件的线性加速度阈值 1
    magnetic_thre = 200  # 判断磁力计是否突变的阈值 200
    f_stroke_thre_std = 8  # 判断是否只有线性加速度计变化，而磁力计没有变化的磁力计阈值 8
    f_stroke_thre_m = 20  # 判断是否只有线性加速度计变化，而磁力计没有变化的磁力计阈值 100

    @classmethod
    def write_file(cls, data, filename="iss.txt"):
        file = open(filename, 'w')
        for r in data:
            for item in r:
                file.write(str(item) + ',')
            file.write("\n")
        file.close()

    # 判断是否发生stroken事件
    @classmethod
    def is_tap(cls, data, thre):
        np_data = np.array(data)
        # 求x,y,z轴两两元素之差
        xyz_dif = np.diff(np_data[:, [2, 3, 4]], axis=0)
        xyz_dot_sum = np.sum(xyz_dif * xyz_dif)
        if xyz_dot_sum > thre:  # tap阈值设置
            return True
        else:
            return False

    # 滑动窗口
    @classmethod
    def slide_win(cls, data, rate, win_time):
        while data[-1][1] - data[0][1] > win_time * rate:
            data.pop(0)

    # 判断是否只有线性加速度变化，而磁力计没有变化的情况
    @classmethod
    def is_false_stroke(cls, data):
        np_d = np.array(data)
        # false stroke
        f_dis = np.std(np_d[:, 2]) + np.std(np_d[:, 3]) + np.std(np_d[:, 4])
        if f_dis < cls.f_stroke_thre_std:
            print('false stroke{ f_dis: %f}' % f_dis)
            return False
        else:
            return True

import threading
import time
from Controller import *


class SensorDetectThread(threading.Thread):
    def __init__(self, conn, dq, recognizerThread):
        threading.Thread.__init__(self)
        self.conn = conn
        self.existFlag = False
        t = time.time()
        self.dataQueue = dq
        self.remainStr = ""
        self.recorderData = []
        print("Start timestamp:%d" % int(round(1000*t)))
        self.recogThread = recognizerThread

    def run(self):
        print("Start detection....")
        while not self.existFlag:
            data_str = self.conn.recv(1024).decode('utf-8')
            if "" == data_str:
                self.existFlag = True
                break
            data_str = self.remainStr + data_str
            data_str_a = data_str.split("\n")
            self.existFlag = False
            if len(data_str_a) == 1:  # maybe the str is not complete
                self.remainStr = data_str
                if 'E' == data_str[0]:
                    print("E")
                    self.existFlag = True
            else:
                for i in range(len(data_str_a) - 1):
                    str_a = data_str_a[i].split(",")
                    item_a = list(map(eval, str_a[1:]))  # ignore the first cell "S" or "E"
                    self.recorderData.append(item_a)
                    self.dataQueue.put(item_a)
                    if 'E' == str_a[0]:
                        print("E")
                        self.existFlag = True
                # keep the last str item
                self.remainStr = data_str_a[-1]
        print("Stop detection.")
        Controller.write_file(self.recorderData, "runtime.txt")
        self.recogThread.exitFlag = True


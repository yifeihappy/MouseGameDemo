import threading
import time
import numpy as np


class ISSThread(threading.Thread):
    def __init__(self, conn, data_controller):
        threading.Thread.__init__(self)
        self.conn = conn
        self.dataController = data_controller
        self.exitFlag = False
        t = time.time()
        print("ISS Start timestamp:%d" % int(round(t*1000)))

    def run(self):
        while not self.exitFlag:
            data_str = self.conn.recv(1024).decode('utf-8')
            print("data:%s" % data_str)
            if "" == data_str:
                self.exitFlag = True
                break
            self.exitFlag = self.dataController.decode_str(data_str)
        t = time.time()
        print("ISS End timestamp:%d" % int(round(t*1000)))
        self.dataController.train_model_iss()
        self.conn.close()


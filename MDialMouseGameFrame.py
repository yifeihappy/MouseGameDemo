import wx
import random
import time
import _thread
from MDialAbstractGameFrame import *
import socket
from ISSThread import *
from ISSDataController import *
from SensorDetectThread import *
import queue
from RecognizerThread import *

# 实时keystroke 识别系统,将输出作为打地鼠程序的输入


class MouseGameFrame(MDialAbstractGameFrame):
    def __init__(self, parent):
        MDialAbstractGameFrame.__init__(self, parent)
        self.game_state = True
        self.button_id = -1
        # hostname = socket.gethostname()
        # self.ip = socket.gethostbyname(hostname)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            self.ip = s.getsockname()[0]
        finally:
            s.close()

        port = 8123
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.ip, port))
        self.s.listen(5)
        self.m_staticText_IP_value.SetLabel(self.ip)


    def change_button_image(self, button_id, image):
        self.m_bpButton_list[button_id].SetBitmap(image)

    def add_right(self):
        self.m_staticText_right.SetLabel(str(int(self.m_staticText_right.GetLabel()) + 1))

    def add_error(self):
        self.m_staticText_error.SetLabel(str(int(self.m_staticText_error.GetLabel()) + 1))

    def change_digit(self, digit):
        self.m_staticText_digit.SetLabel(digit)

    def __reset_static_text(self):
        self.m_staticText_digit.SetLabel('')
        self.m_staticText_error.SetLabel('0')
        self.m_staticText_right.SetLabel('0')

    # Virtual event handlers, overide them in your derived class
    def start_game(self, event):
        self.game_state = True
        _thread.start_new_thread(start_game_thread, (self,))
        self.m_button_start.Disable()
        self.m_button_stop.Enable()

    def stop_game(self, event):
        self.game_state = False
        self.__reset_static_text()
        self.m_button_stop.Disable()
        self.m_button_start.Enable()

    def button_click(self, event):
        print("click")
        print(event.GetEventObject().GetLabel())
        button_id = int(event.GetEventObject().GetLabel())
        if self.button_id == button_id:
            self.add_right()
            self.change_button_image(button_id, self.image_hit)
        else:
            self.add_error()
        self.change_digit(str(button_id))

    def iss_thread(self, event):
        print("ISS click")
        #     显示IP
        print(self.ip)
        self.m_button_ISS.Disable()
        conn, add = self.s.accept()
        iSSDataController = ISSDataController(self)
        iSSThread = ISSThread(conn, iSSDataController)
        iSSThread.start()
        self.m_button_ISS.Enable()

    def server_thread(self, event):
        self.m_button_SERVER.Disable()
        conn, add = self.s.accept()
        dataQueue = queue.Queue(maxsize=0)
        recognizerThread = RecognizerThread(dataQueue, self)
        recognizerThread.start()
        sensorDetectThread = SensorDetectThread(conn, dataQueue, recognizerThread)
        sensorDetectThread.start()
        self.m_button_start.Enable()
        self.m_button_stop.Enable()
        self.m_button_SERVER.Enable()


def start_game_thread(frame):
    while frame.game_state:
        frame.button_id = random.randint(0, 8)
        frame.change_button_image(frame.button_id, frame.image_mouse)
        sleep_time = (random.random() + 0.5)*2
        time.sleep(sleep_time)
        frame.change_button_image(frame.button_id, frame.image_hole)


if __name__ == "__main__":
    app = wx.App(False)
    frame = MouseGameFrame(None)
    frame.Center()
    frame.Show(True)
    app.MainLoop()

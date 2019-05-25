import wx
import random
import time
import _thread

from AbstractGameFrame import *


class MouseGameFrame(AbstractGameFrame):
    def __init__(self, parent):
        AbstractGameFrame.__init__(self, parent)
        self.game_state = True
        self.button_id = -1

    def change_button_image(self, button_id, image):
        self.m_bpButton_list[button_id].SetBitmap(image)

    def __add_right(self):
        self.m_staticText_right.SetLabel(str(int(self.m_staticText_right.GetLabel()) + 1))

    def __add_error(self):
        self.m_staticText_error.SetLabel(str(int(self.m_staticText_error.GetLabel()) + 1))

    def __change_digit(self, digit):
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

    # # 调用其它button的click函数
    # def click_btn1(self, event):
    #     self.m_button_start.ProcessEvent(wx.CommandEvent(wx.EVT_BUTTON.typeId, self.m_button_start.GetId()))

    def button_click(self, event):
        print("click")
        print(event.GetEventObject().GetLabel())
        button_id = int(event.GetEventObject().GetLabel())
        if self.button_id == button_id:
            self.__add_right()
            self.change_button_image(button_id, self.image_hit)
        else:
            self.__add_error()
        self.__change_digit(str(button_id))


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

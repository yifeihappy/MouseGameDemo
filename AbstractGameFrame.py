# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class GameFrame
###########################################################################

class AbstractGameFrame(wx.Frame):

    def __init__(self, parent):
        # 设定Frame 大小
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(519, 482), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHints(wx.Size(519, 482), wx.Size(519, 482))
        # 总体布局
        bSizer_all = wx.BoxSizer(wx.VERTICAL)

        # top 布局
        bSizer_top = wx.BoxSizer(wx.HORIZONTAL)
        # 得分 布局
        bSizer_right = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"RIGHT", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(wx.Font(20, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText1.SetForegroundColour(wx.Colour(0, 255, 128))

        bSizer_right.Add(self.m_staticText1, 1, wx.ALL, 5)

        self.m_staticText_right = wx.StaticText(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_right.Wrap(-1)
        self.m_staticText_right.SetFont(wx.Font(20, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText_right.SetForegroundColour(wx.Colour(0, 255, 128))

        bSizer_right.Add(self.m_staticText_right, 1, wx.ALL, 5)

        bSizer_top.Add(bSizer_right, 1, wx.EXPAND, 5)

        # error 布局
        bSizer_error = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"ERROR", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(wx.Font(20, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText3.SetForegroundColour(wx.Colour(255, 0, 0))

        bSizer_error.Add(self.m_staticText3, 1, wx.ALL, 5)

        self.m_staticText_error = wx.StaticText(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_error.Wrap(-1)
        self.m_staticText_error.SetFont(wx.Font(20, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText_error.SetForegroundColour(wx.Colour(255, 0, 0))

        bSizer_error.Add(self.m_staticText_error, 1, wx.ALL, 5)

        bSizer_top.Add(bSizer_error, 1, wx.EXPAND, 5)

        # digit 布局
        bSizer_digit = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"DIGIT", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        self.m_staticText5.SetFont(wx.Font(20, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText5.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        bSizer_digit.Add(self.m_staticText5, 1, wx.ALL, 5)

        self.m_staticText_digit = wx.StaticText(self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_digit.Wrap(-1)
        self.m_staticText_digit.SetFont(wx.Font(20, 70, 90, 90, False, wx.EmptyString))

        bSizer_digit.Add(self.m_staticText_digit, 1, wx.ALL, 5)

        bSizer_top.Add(bSizer_digit, 1, wx.EXPAND, 5)

        bSizer_all.Add(bSizer_top, 0, wx.EXPAND, 5)

        gSizer_middle = wx.GridSizer(3, 3, 0, 0)

        image_hole_url = u"C:\\Users\\14776\\Pictures\\Camera Roll\\hide.bmp"
        image_mouse_url = u"C:\\Users\\14776\\Pictures\\Camera Roll\\out.bmp"
        image_hit_url = u"C:\\Users\\14776\\Pictures\\Camera Roll\\hit.bmp"

        self.image_hole = wx.Bitmap(image_hole_url, wx.BITMAP_TYPE_ANY)
        self.image_mouse = wx.Bitmap(image_mouse_url, wx.BITMAP_TYPE_ANY)
        self.image_hit = wx.Bitmap(image_hit_url, wx.BITMAP_TYPE_ANY)

        self.m_bpButton_list = []
        for i in range(9):
            self.m_bpButton_list.append(wx.BitmapButton(self, wx.ID_ANY, self.image_hole, wx.DefaultPosition,
                                                        wx.DefaultSize, wx.BU_AUTODRAW))

            gSizer_middle.Add(self.m_bpButton_list[i], 0, wx.ALL, 5)

        bSizer_all.Add(gSizer_middle, 1, wx.ALIGN_CENTER, 5)

        bSizer_bottom = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button_start = wx.Button(self, wx.ID_ANY, u"START", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer_bottom.Add(self.m_button_start, 1, wx.ALL, 10)

        self.m_button_stop = wx.Button(self, wx.ID_ANY, u"STOP", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button_stop.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        bSizer_bottom.Add(self.m_button_stop, 1, wx.ALL, 10)

        # self.m_button_click = wx.Button(self, wx.ID_ANY, u"CLICK", wx.DefaultPosition, wx.DefaultSize, 0)
        # bSizer_bottom.Add(self.m_button_click, 1, wx.ALL, 10)

        bSizer_all.Add(bSizer_bottom, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER | wx.EXPAND, 5)

        self.SetSizer(bSizer_all)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button_start.Bind(wx.EVT_BUTTON, self.start_game)
        self.m_button_stop.Bind(wx.EVT_BUTTON, self.stop_game)
        # self.m_button_click.Bind(wx.EVT_BUTTON, self.click_btn1)

        for i in range(9):
            self.m_bpButton_list[i].Bind(wx.EVT_BUTTON, self.button_click)
            self.m_bpButton_list[i].SetLabel(str(i))

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def start_game(self, event):
        event.Skip()

    def stop_game(self, event):
        event.Skip()

    def button_click(self, event):
        event.Skip()

    def click_btn1(self, event):
        event.Skip()



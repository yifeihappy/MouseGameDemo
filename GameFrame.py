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

class GameFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(519, 482), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(519, 482), wx.Size(519, 482))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"RIGHT", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(wx.Font(20, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText1.SetForegroundColour(wx.Colour(0, 255, 128))

        bSizer2.Add(self.m_staticText1, 1, wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetFont(wx.Font(20, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText2.SetForegroundColour(wx.Colour(0, 255, 128))

        bSizer2.Add(self.m_staticText2, 1, wx.ALL, 5)

        bSizer5.Add(bSizer2, 1, wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"ERROR", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(wx.Font(20, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText3.SetForegroundColour(wx.Colour(255, 0, 0))

        bSizer3.Add(self.m_staticText3, 1, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        self.m_staticText4.SetFont(wx.Font(20, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText4.SetForegroundColour(wx.Colour(255, 0, 0))

        bSizer3.Add(self.m_staticText4, 1, wx.ALL, 5)

        bSizer5.Add(bSizer3, 1, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"DIGIT", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        self.m_staticText5.SetFont(wx.Font(20, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText5.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        bSizer4.Add(self.m_staticText5, 1, wx.ALL, 5)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        self.m_staticText6.SetFont(wx.Font(20, 70, 90, 90, False, wx.EmptyString))

        bSizer4.Add(self.m_staticText6, 1, wx.ALL, 5)

        bSizer5.Add(bSizer4, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer5, 0, wx.EXPAND, 5)

        gSizer1 = wx.GridSizer(3, 3, 0, 0)

        self.m_bpButton1 = wx.BitmapButton(self, wx.ID_ANY,
                                           wx.Bitmap(u"C:\\Users\\14776\\Pictures\\Camera Roll\\hole.bmp",
                                                     wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize,
                                           wx.BU_AUTODRAW)
        gSizer1.Add(self.m_bpButton1, 0, wx.ALL, 5)

        self.m_bpButton2 = wx.BitmapButton(self, wx.ID_ANY,
                                           wx.Bitmap(u"C:\\Users\\14776\\Pictures\\Camera Roll\\hole.bmp",
                                                     wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize,
                                           wx.BU_AUTODRAW)
        gSizer1.Add(self.m_bpButton2, 0, wx.ALL, 5)

        self.m_bpButton3 = wx.BitmapButton(self, wx.ID_ANY,
                                           wx.Bitmap(u"C:\\Users\\14776\\Pictures\\Camera Roll\\hole.bmp",
                                                     wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize,
                                           wx.BU_AUTODRAW)
        gSizer1.Add(self.m_bpButton3, 0, wx.ALL, 5)

        self.m_bpButton4 = wx.BitmapButton(self, wx.ID_ANY,
                                           wx.Bitmap(u"C:\\Users\\14776\\Pictures\\Camera Roll\\hole.bmp",
                                                     wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize,
                                           wx.BU_AUTODRAW)
        gSizer1.Add(self.m_bpButton4, 0, wx.ALL, 5)

        self.m_bpButton5 = wx.BitmapButton(self, wx .ID_ANY,
                                           wx.Bitmap(u"C:\\Users\\14776\\Pictures\\Camera Roll\\hole.bmp",
                                                     wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize,
                                           wx.BU_AUTODRAW)
        gSizer1.Add(self.m_bpButton5, 0, wx.ALL, 5)

        self.m_bpButton6 = wx.BitmapButton(self, wx.ID_ANY,
                                           wx.Bitmap(u"C:\\Users\\14776\\Pictures\\Camera Roll\\hole.bmp",
                                                     wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize,
                                           wx.BU_AUTODRAW)
        gSizer1.Add(self.m_bpButton6, 0, wx.ALL, 5)

        self.m_bpButton7 = wx.BitmapButton(self, wx.ID_ANY,
                                           wx.Bitmap(u"C:\\Users\\14776\\Pictures\\Camera Roll\\hole.bmp",
                                                     wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize,
                                           wx.BU_AUTODRAW)
        gSizer1.Add(self.m_bpButton7, 0, wx.ALL, 5)

        self.m_bpButton8 = wx.BitmapButton(self, wx.ID_ANY,
                                           wx.Bitmap(u"C:\\Users\\14776\\Pictures\\Camera Roll\\hole.bmp",
                                                     wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize,
                                           wx.BU_AUTODRAW)
        gSizer1.Add(self.m_bpButton8, 0, wx.ALL, 5)

        self.m_bpButton9 = wx.BitmapButton(self, wx.ID_ANY,
                                           wx.Bitmap(u"C:\\Users\\14776\\Pictures\\Camera Roll\\hole.bmp",
                                                     wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize,
                                           wx.BU_AUTODRAW)
        gSizer1.Add(self.m_bpButton9, 0, wx.ALL, 5)

        bSizer1.Add(gSizer1, 1, wx.ALIGN_CENTER, 5)

        bSizer31 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"START", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer31.Add(self.m_button1, 1, wx.ALL, 10)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"STOP", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button2.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        bSizer31.Add(self.m_button2, 1, wx.ALL, 10)

        bSizer1.Add(bSizer31, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button1.Bind(wx.EVT_BUTTON, self.start_game)
        self.m_button2.Bind(wx.EVT_BUTTON, self.stop_game)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def start_game(self, event):
        event.Skip()

    def stop_game(self, event):
        event.Skip()



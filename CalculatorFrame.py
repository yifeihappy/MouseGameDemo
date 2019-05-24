# -*- coding: utf-8 -*-
import wx
import wx.xrc


class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"平方计算器"), wx.VERTICAL)

        self.m_textCtrl1 = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        sbSizer2.Add(self.m_textCtrl1, 0, wx.ALL, 5)

        self.m_button13 = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"求平方", wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer2.Add(self.m_button13, 0, wx.ALL, 5)

        self.m_textCtrl2 = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        sbSizer2.Add(self.m_textCtrl2, 0, wx.ALL, 5)

        self.SetSizer(sbSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button13.Bind(wx.EVT_BUTTON, self.squareFunction)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def squareFunction(self, event):
        event.Skip()



import CalculatorFrame
import wx


class CalcFrame(CalculatorFrame.MyFrame1):
    def __init__(self, parent):
        CalculatorFrame.MyFrame1.__init__(self, parent)

    def squareFunction(self, event):
        num = int(self.m_textCtrl1.GetValue())
        self.m_textCtrl2.SetValue(str(num * num))


if __name__ == "__main__":
    app = wx.App(False)
    frame = CalcFrame(None)
    frame.Show(True)
    app.MainLoop()

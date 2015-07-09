#!/usr/bin/python

import wx

#######################################################################
class Frame(wx.Frame):
    ###################################################################
    def __init__(self, parent,title="AutoFence",size=(480,320)):
        wx.Frame.__init__(self,parent,title=title,size=size)
        self.menu = wx.Menu()
        menuAbout = self.menu.Append(wx.ID_ABOUT,"&About",\
                "The AutoFence: \nBy Clarke's Building")
        self.menu.AppendSeparator()
        menuExit = self.menu.Append(wx.ID_EXIT,"E&xit",\
                "Exit AutoFence")
        menuBar = wx.MenuBar()
        menuBar.Append(self.menu, "&File")
        self.SetMenuBar(menuBar)
        self.Show(True)
#######################################################################
if __name__ == "__main__":
    app = wx.App(False)
    frame = Frame(None)
    app.MainLoop()

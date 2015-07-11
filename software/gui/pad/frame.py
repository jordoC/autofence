#!/usr/bin/python

import wx
from panel import PadPanel
#######################################################################
class Frame(wx.Frame):
    ###################################################################
    def __init__(self, parent,title="AutoFence",size=(480,320)):
        wx.Frame.__init__(self,parent,title=title,size=size)
        self.menu = wx.Menu()
        menuAbout = self.menu.Append(wx.ID_ABOUT,"&About",\
                "The AutoFence: \nBy Clarke's Building")
        self.Bind(wx.EVT_MENU, self.onAbout, menuAbout)
        self.menu.AppendSeparator()
        menuExit = self.menu.Append(wx.ID_EXIT,"E&xit",\
                "Exit AutoFence")
        self.Bind(wx.EVT_MENU, self.onExit, menuExit)
        menuBar = wx.MenuBar()
        menuBar.Append(self.menu, "&File")
        self.SetMenuBar(menuBar)
        self.Show(True)
    ###################################################################
    def onAbout(self, event):
        aboutDialog = wx.MessageDialog(self,\
                "The AutoFence: By Clarke's Building", "About", wx.OK)
        aboutDialog.ShowModal()
        aboutDialog.Destroy()
    ###################################################################
    def onExit(self, event):
        self.Close(True)
#######################################################################
if __name__ == "__main__":
    app = wx.App(False)
    frame = Frame(None)
    panel = PadPanel(frame)
    app.MainLoop()

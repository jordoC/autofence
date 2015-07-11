#!/usr/bin/python

import wx
#######################################################################
class PadPanel(wx.Panel):
    ###################################################################
    def __init__(self, parent):
	wx.Panel.__init__(self, parent)
	self.grid = wx.GridBagSizer(hgap=2, vgap=2)
	self._xpos = 0
	self._ypos = 0
	self.button0 = wx.Button(self, label = "0")
	self.button1 = wx.Button(self, label = "1")
	self.button2 = wx.Button(self, label = "2")
	self.button3 = wx.Button(self, label = "3")
	self.button4 = wx.Button(self, label = "4")
	self.button5 = wx.Button(self, label = "5")
	self.button6 = wx.Button(self, label = "6")
	self.button7 = wx.Button(self, label = "7")
	self.button8 = wx.Button(self, label = "8")
	self.button9 = wx.Button(self, label = "9")
	self.buttonDec = wx.Button(self, label = ".")
	self.buttonClr = wx.Button(self, label = "Clear")
	self.display = wx.TextCtrl(self, size=(300, 25), style=wx.TE_READONLY)
	self.alignBindPanel()
    ###################################################################
    def alignBindPanel(self):
	#Add in the display
	self._addGuiRow(self.display)
#	self.grid.Add(self.button1, pos=(0,0))
	#Add in the buttons
	self._addGuiCell(self.button1)
#	self.grid.Add(self.button2, pos=(1,1))
	self._addGuiCell(self.button2)
	self._addGuiCell(self.button3)
	self._incGuiRow()
	self._addGuiCell(self.button4)
	self._addGuiCell(self.button5)
	self._addGuiCell(self.button6)
	self._incGuiRow()
	self._addGuiCell(self.button7)
	self._addGuiCell(self.button8)
	self._addGuiCell(self.button9)
	self._incGuiRow()
	self._addGuiCell(self.buttonDec)
	self._addGuiCell(self.button0)
	self._addGuiCell(self.buttonClr)
	#Bind the buttons
	self.Bind(wx.EVT_BUTTON, self.onButton1, self.button1)
	self.Bind(wx.EVT_BUTTON, self.onButton2, self.button2)
	self.Bind(wx.EVT_BUTTON, self.onButton3, self.button3)
	self.Bind(wx.EVT_BUTTON, self.onButton4, self.button4)
	self.Bind(wx.EVT_BUTTON, self.onButton5, self.button5)
	self.Bind(wx.EVT_BUTTON, self.onButton6, self.button6)
	self.Bind(wx.EVT_BUTTON, self.onButton7, self.button7)
	self.Bind(wx.EVT_BUTTON, self.onButton8, self.button8)
	self.Bind(wx.EVT_BUTTON, self.onButton9, self.button9)
	self.Bind(wx.EVT_BUTTON, self.onButton0, self.button0)
	self.Bind(wx.EVT_BUTTON, self.onButtonDec, self.buttonDec)
	self.Bind(wx.EVT_BUTTON, self.onButtonClr, self.buttonClr)
	self.SetSizerAndFit(self.grid)
	print "Done align and bind"
    ###################################################################
    def onButton1(self, event):
	self._updateDisplay(value="1")
    ###################################################################
    def onButton2(self, event):
	self._updateDisplay(value="2")
    ###################################################################
    def onButton3(self, event):
	self._updateDisplay(value="3")
    ###################################################################
    def onButton4(self, event):
	self._updateDisplay(value="4")
    ###################################################################
    def onButton5(self, event):
	self._updateDisplay(value="5")
    ###################################################################
    def onButton6(self, event):
	self._updateDisplay(value="6")
    ###################################################################
    def onButton7(self, event):
	self._updateDisplay(value="7")
    ###################################################################
    def onButton8(self, event):
	self._updateDisplay(value="8")
    ###################################################################
    def onButton9(self, event):
	self._updateDisplay(value="9")
    ###################################################################
    def onButton0(self, event):
	self._updateDisplay(value="0")
    ###################################################################
    def onButtonDec(self, event):
	self._updateDisplay(value=".")
    ###################################################################
    def onButtonClr(self, event):
	self._updateDisplay(clear=True)
    ###################################################################
    ###################LOCAL METHODS/HELPERS###########################
    ###################################################################
    def _addGuiRow(self, guiElement):
	self.grid.Add(guiElement, pos=(self._ypos,self._xpos), span=(1,3))
	self._xpos = 0
	self._ypos += 1
    ###################################################################
    def _addGuiCell(self, guiElement):
	self.grid.Add(guiElement, pos=(self._ypos,self._xpos))
	self._xpos += 1
    ###################################################################
    def _incGuiRow (self):
	self._xpos = 0
	self._ypos += 1
    ###################################################################
    def _incGuiCell (self):
	self._xpos += 1
    ###################################################################
    def _updateDisplay(self, value="", clear=False):
	if clear is True:
	    self.display.Clear()
	else:
	    self.display.SetInsertionPointEnd()
	    self.display.write(value)
#######################################################################
if __name__ == "__main__":
    print "Main"
    app = wx.App(False)
    frame = wx.Frame(None)
    panel = PadPanel(frame)
    frame.Show()
    app.MainLoop()

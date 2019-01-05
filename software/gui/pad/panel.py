#!/usr/bin/python

"""This module contains a class for the numerical pad GUI for
setting and getting fence position."""

__license__ = "None"
__revision__ = "0.0.1"
__docformat__ = 'reStructuredText'

import wx
from time import sleep
#######################################################################
class PadPanel(wx.Panel):
    """Numerical pad for setting/getting fence position

    The PadPanel class is a standard 10-digit numerical pad (similar
    to a calculator) inteded for setting and getting the position of
    the fence. Both imperial and metric inputs are supported. Class
    uses the Python wx library for building the GUI.

    - **parameters**, **types**::

            :param wx.Panel: Panel object the class inherits from
            :type wx.Panel: A Panel object from the wx library

    """
    ###################################################################
    ################## MEMBER METHODS #################################
    ###################################################################
    def __init__(self, parent):
        """Constructor to build/initialze the GUI
            
            :param self: Instance of this class, this is modifying
                         method
            :param parent:  Parent object that this class inherits
                            from. In this case wx.Panel object.
            :type PadPanel: This class.
            :type wx.Panel: A Panel object from the wx library
        """
        #Intialize parent
	wx.Panel.__init__(self, parent)
        #Setup grid
	self.grid = wx.GridBagSizer(hgap=2, vgap=2)
        #Initialize members
	self._xpos = 0
	self._ypos = 0
	self.fencePos=None
	self.isMetric=True
	self.display = wx.TextCtrl(self, size=(260, 25), style=wx.TE_READONLY)
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
	self.buttonSetFencePos= wx.Button(self, label = "Set Position")
	self.buttonGetFencePos= wx.Button(self, label = "Get Position")
	#NOTE: order of this list matters: 0-->metric, 1-->imperial
	self.metricImperialList = ['Metric (mm)', 'Imperial (inch)']
	self.metricImperial = wx.RadioBox(self, label="System of Measure",\
		choices=self.metricImperialList, majorDimension=2, style=wx.RA_SPECIFY_COLS)
	self.alignBindPanel()
    ###################################################################
    def alignBindPanel(self):
        """Align the GUI elements and bind them to functions
            
            :param self: Instance of this class, this is modifying
                         method
            :type PadPanel: This class.
        """
	#Add in the display
	self._addGuiRow(self.display)
	
        #Add in the buttons
	self._addGuiCell(self.button1)
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
	self._incGuiRow()
	self._addGuiCell(self.buttonSetFencePos)
	self._addGuiCell(self.buttonGetFencePos)
	self._incGuiRow()
	self._addGuiRow(self.metricImperial)
	
        #Bind the buttons to functions
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
	self.Bind(wx.EVT_BUTTON, self.onButtonSetFencePos, self.buttonSetFencePos)
	self.Bind(wx.EVT_BUTTON, self.onButtonGetFencePos, self.buttonGetFencePos)
	self.Bind(wx.EVT_RADIOBOX, self.onMetricImperial, self.metricImperial)
	self.SetSizerAndFit(self.grid)
    ###################################################################
    def onButton1(self, event):
        """Binding function that updates display for button 1
            
            :param self: Instance of this class, this is modifying
                         method
            :param event:   GUI event that corresponds to a button press 
            :type PadPanel: This class.
            :type wx.EVT_BUTTON:    An button press event from the wx 
                                    GUI library. 
        """
	self._updateDisplay(value="1")
    ###################################################################
    def onButton2(self, event):
        """Binding function that updates display for button 2
            
            :param self: Instance of this class, this is modifying
                         method
            :param event:   GUI event that corresponds to a button press 
            :type PadPanel: This class.
            :type wx.EVT_BUTTON:    An button press event from the wx 
                                    GUI library. 
        """
	self._updateDisplay(value="2")
    ###################################################################
    def onButton3(self, event):
        """Binding function that updates display for button 3
            
            :param self: Instance of this class, this is modifying
                         method
            :param event:   GUI event that corresponds to a button press 
            :type PadPanel: This class.
            :type wx.EVT_BUTTON:    An button press event from the wx 
                                    GUI library. 
        """
	self._updateDisplay(value="3")
    ###################################################################
    def onButton4(self, event):
        """Binding function that updates display for button 4
            
            :param self: Instance of this class, this is modifying
                         method
            :param event:   GUI event that corresponds to a button press 
            :type PadPanel: This class.
            :type wx.EVT_BUTTON:    An button press event from the wx 
                                    GUI library. 
        """
	self._updateDisplay(value="4")
    ###################################################################
    def onButton5(self, event):
        """Binding function that updates display for button 5
            
            :param self: Instance of this class, this is modifying
                         method
            :param event:   GUI event that corresponds to a button press 
            :type PadPanel: This class.
            :type wx.EVT_BUTTON:    An button press event from the wx 
                                    GUI library. 
        """
	self._updateDisplay(value="5")
    ###################################################################
    def onButton6(self, event):
        """Binding function that updates display for button 6
            
            :param self: Instance of this class, this is modifying
                         method
            :param event:   GUI event that corresponds to a button press 
            :type PadPanel: This class.
            :type wx.EVT_BUTTON:    An button press event from the wx 
                                    GUI library. 
        """
	self._updateDisplay(value="6")
    ###################################################################
    def onButton7(self, event):
        """Binding function that updates display for button 7
            
            :param self: Instance of this class, this is modifying
                         method
            :param event:   GUI event that corresponds to a button press 
            :type PadPanel: This class.
            :type wx.EVT_BUTTON:    An button press event from the wx 
                                    GUI library. 
        """
	self._updateDisplay(value="7")
    ###################################################################
    def onButton8(self, event):
        """Binding function that updates display for button 8
            
            :param self: Instance of this class, this is modifying
                         method
            :param event:   GUI event that corresponds to a button press 
            :type PadPanel: This class.
            :type wx.EVT_BUTTON:    An button press event from the wx 
                                    GUI library. 
        """
	self._updateDisplay(value="8")
    ###################################################################
    def onButton9(self, event):
        """Binding function that updates display for button 9
            
            :param self: Instance of this class, this is modifying
                         method
            :param event:   GUI event that corresponds to a button press 
            :type PadPanel: This class.
            :type wx.EVT_BUTTON:    An button press event from the wx 
                                    GUI library. 
        """
	self._updateDisplay(value="9")
    ###################################################################
    def onButton0(self, event):
        """Binding function that updates display for button 0
            
            :param self: Instance of this class, this is modifying
                         method
            :param event:   GUI event that corresponds to a button press 
            :type PadPanel: This class.
            :type wx.EVT_BUTTON:    An button press event from the wx 
                                    GUI library. 
        """
	self._updateDisplay(value="0")
    ###################################################################
    def onButtonDec(self, event):
        """Binding function that updates display for button .
            
            :param self: Instance of this class, this is modifying
                         method
            :param event:   GUI event that corresponds to a button press 
            :type PadPanel: This class.
            :type wx.EVT_BUTTON:    An button press event from the wx 
                                    GUI library. 
        """
	self._updateDisplay(value=".")
    ###################################################################
    def onButtonClr(self, event):
        """Binding function that updates display for clear button 
            
            :param self: Instance of this class, this is modifying
                         method
            :param event:   GUI event that corresponds to a button press 
            :type PadPanel: This class.
            :type wx.EVT_BUTTON:    An button press event from the wx 
                                    GUI library. 
        """
	self._updateDisplay(clear=True)
    ###################################################################
    def onButtonSetFencePos(self, event):
        """Binding function that sets fence position
            
            :param self: Instance of this class, this is modifying
                         method
            :param event:   GUI event that corresponds to a button press 
            :type PadPanel: This class.
            :type wx.EVT_BUTTON:    An button press event from the wx 
                                    GUI library. 
        """
        val = self.display.GetValue()
        if self.display.IsEmpty() is True:
            pass
        else:
            self.fencePos = float(val)
    ###################################################################
    def onButtonGetFencePos(self, event):
        """Binding function that gets fence position
            
            :param self: Instance of this class, this is modifying
                         method
            :param event:   GUI event that corresponds to a button press 
            :type PadPanel: This class.
            :type wx.EVT_BUTTON:    An button press event from the wx 
                                    GUI library. 
        """
        if self.fencePos is None:
            self._updateDisplay(value=str("Fence is not Set"), clear=True)
        else:
            self._updateDisplay(value=str(self.fencePos), clear=True)
        
    ###################################################################
    def onMetricImperial(self, event):
        """Binding function that gets fence position
            
            :param self: Instance of this class, this is modifying
                         method
            :param event:   GUI event that corresponds to a button press 
            :type PadPanel: This class.
            :type wx.EVT_RADIOBOX: A radiobox event from the wx 
                                    GUI library. 
        """
        val = self.display.GetValue()
        if (self.metricImperial.GetSelection() == 0):
            if self.display.IsEmpty() is True:
                self.isMetric = True 
            else:
                #NOTE: 25.4mm/inch
                self.fencePos = float(val)*25.4
                imperialVal = float(val)
                metricVal = str(imperialVal*25.4)
                self._updateDisplay(value=metricVal, clear=True)
                self.isMetric = True 
        else:
            if self.display.IsEmpty() is True:
                self.isMetric = False 
            else:
                #NOTE: 25.4mm/inch
                self.fencePos = float(val)/25.4
                metricVal = float(val)
                imperialVal = str(metricVal/25.4)
                self._updateDisplay(value=imperialVal, clear=True)
                self.isMetric = False

    ###################################################################
    ###################LOCAL METHODS/HELPERS###########################
    ###################################################################
    def _addGuiRow(self, guiElement):
        """Method for adding an element to a new row of the GUI grid
            
            :param self: Instance of this class, this is modifying
                         method
            :param guiElement:  GUI element to be added to the new row
            :type PadPanel: This class.
            :type wx.RadioBox, wx.Button:   A radiobox or button from the 
                                            wx GUI library. 
        """
	self.grid.Add(guiElement, pos=(self._ypos,self._xpos), span=(1,3))
	self._xpos = 0
	self._ypos += 1
    ###################################################################
    def _addGuiCell(self, guiElement):
        """Method for adding an element to a new cell of the GUI grid
            
            :param self: Instance of this class, this is modifying
                         method
            :param guiElement:  GUI element to be added to the new row
            :type PadPanel: This class.
            :type wx.RadioBox, wx.Button:   A radiobox or button from the 
                                            wx GUI library. 
        """
	self.grid.Add(guiElement, pos=(self._ypos,self._xpos))
	self._xpos += 1
    ###################################################################
    def _incGuiRow (self):
        """Method for skipping a row in ghe GUI grid
            
            :param self: Instance of this class, this is modifying
                         method
            :type PadPanel: This class.
        """
	self._xpos = 0
	self._ypos += 1
    ###################################################################
    def _incGuiCell (self):
        """Method for skipping a cell in ghe GUI grid
            
            :param self: Instance of this class, this is modifying
                         method
            :type PadPanel: This class.
        """
	self._xpos += 1
    ###################################################################
    def _updateDisplay(self, value="", clear=False):
        """Method for updating the GUI display
            
            :param self: Instance of this class, this is modifying
                         method
            :param value:   Value which we want to update the screen to,
                            defaults to "" 
            :param clear:   Function to clear the display 
            :type PadPanel: This class.
            :type String:   Standard string value 
            :type Boolean:  Standard boolean value
        """
	if clear is True:
	    self.display.Clear()
    	self.display.SetInsertionPointEnd()
    	self.display.write(value)
#######################################################################

################ STAND-ALONE CALL STRUCTURE FOR TEST: #################
if __name__ == "__main__":
    app = wx.App(False)
    frame = wx.Frame(None)
    panel = PadPanel(frame)
    frame.Show()
    app.MainLoop()

#!/usr/bin/python
"""This module contains a class for the numerical pad GUI for
setting and getting fence position with a menu."""

__license__ = "None"
__revision__ = "0.0.1"
__docformat__ = 'reStructuredText'

import wx
from panel import PadPanel
#######################################################################
class Frame(wx.Frame):
    """Frame for setting/getting fence position

    The frame adds a menu to the numerical pad panel for additional
    functionality.

    - **parameters**, **types**::

            :param wx.Frame:    Frame object the class inherits from
            :type wx.Frame: A Frame object from the wx library

    """
    ###################################################################
    def __init__(self, parent,title="AutoFence",size=(320,240)):
        """Constructor to build/initialze the GUI
            
            :param self:    Instance of this class, this is modifying
                            method
            :param parent:  Parent object that this class inherits
                            from. In this case wx.Panel object.
            :param title:   Name for the menu bar
            :param size:    (x,y) cartesian pair in pixels that
                            specifies size of the frame 
            :type Frame:    This class.
            :type wx.Frame: A Frame object from the wx library
            :type String:   Standard string value 
            :type Tuple:    Tuple of two integer values
        """
        wx.Frame.__init__(self,parent,title=title,size=size)
        self.menu = wx.Menu()
        menuAbout = self.menu.Append(wx.ID_ABOUT,"&About",\
                "The AutoFence: \nBy Clarke's Building")
        self.Bind(wx.EVT_MENU, self._onAbout, menuAbout)
        self.menu.AppendSeparator()
        menuExit = self.menu.Append(wx.ID_EXIT,"E&xit",\
                "Exit AutoFence")
        self.Bind(wx.EVT_MENU, self._onExit, menuExit)
        menuBar = wx.MenuBar()
        menuBar.Append(self.menu, "&File")
        self.SetMenuBar(menuBar)
        self.Show(True)
    ###################################################################
    def _onAbout(self, event):
        """Binding function shows about information
            
            :param self:    Instance of this class, this is modifying
                            method
            :param event:   GUI event that corresponds to a button press 
            :type Frame:    This class.
            :type wx.EVT_MENU:    An menu press event from the wx 
                                  GUI library. 
        """
        aboutDialog = wx.MessageDialog(self,\
                "The AutoFence: By Clarke's Building", "About", wx.OK)
        aboutDialog.ShowModal()
        aboutDialog.Destroy()
    ###################################################################
    def _onExit(self, event):
        """Binding function 
            
            :param self:    Instance of this class, this is modifying
                            method
            :param event:   GUI event that corresponds to a button press 
            :type Frame:    This class.
            :type wx.EVT_MENU:    An menu press event from the wx 
                                  GUI library. 
        """
        self.Close(True)
#######################################################################

################ STAND-ALONE CALL STRUCTURE FOR TEST: #################
if __name__ == "__main__":
    app = wx.App(False)
    frame = Frame(None)
    panel = PadPanel(frame)
    app.MainLoop()

import wx

class CoordsFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(CoordsFrame, self).__init__(*args, **kw)

        pnl = wx.Panel(self)

        # Store some values
        self.topLeft = None
        self.bottomRight = None

        # Create our text
        self.actionText = wx.StaticText(pnl, label="Press space to set first corner")
        self.st = wx.StaticText(pnl, label="")
        self.boundingBoxText = wx.StaticText(pnl, label="")
        font = self.st.GetFont()
        font.PointSize += 3
        font = font.Bold()
        self.st.SetFont(font)

        # Create a sizer to handle the layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.actionText, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        sizer.Add(self.st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        sizer.Add(self.boundingBoxText, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        pnl.SetSizer(sizer)

        # Let's capture space bar events
        pnl.Bind(wx.EVT_KEY_DOWN, self.OnKeyPress)

        # Capture mouse position with a timer loop
        self.captureMousePos()

        # Create a pointless menu bar
        self.makeMenuBar()

    def makeMenuBar(self):
        # Make a file menu with an About item
        fileMenu = wx.Menu()
        aboutItem = fileMenu.Append(-1, "&About")
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)

    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)

    def OnAbout(self, event):
        """Print the about info"""
        wx.MessageBox("Screen Coordinate Helper 1.0\nBy Matthew Darby\n\nhttps://github.com/mjdarby/ScreenCoordinateHelper")

    def OnKeyPress(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_SPACE:
            # If top-left isn't set, set it
            if not self.topLeft:
                self.topLeft = self.captureMousePos()
                label = "Top-left of bounding box: {}".format(self.topLeft)
                actionLabel = "Press space to set opposite corner"
                self.boundingBoxText.SetLabel(label)
                self.actionText.SetLabel(actionLabel)
            # If bottom-right isn't set, set it
            elif not self.bottomRight:
                self.bottomRight = self.captureMousePos()
                height, width = (abs(self.topLeft[0] - self.bottomRight[0]),
                                 abs(self.topLeft[1] - self.bottomRight[1]))
                label = "Top-left of bounding box: {}".format(self.topLeft)
                label += "\nBottom-right of bounding box: {}".format(self.bottomRight)
                label += "\nWidth, height of bounding box: {}".format((height, width))
                actionLabel = "Press space to reset"
                self.boundingBoxText.SetLabel(label)
                self.actionText.SetLabel(actionLabel)
            # Otherwise, clear both
            else:
                self.topLeft = None
                self.bottomRight = None
                actionLabel = "Press space to set first corner"
                self.boundingBoxText.SetLabel("")
                self.actionText.SetLabel(actionLabel)
        event.Skip()

    def captureMousePos(self):
        """Returns the current mouse pos"""
        mx, my = wx.GetMousePosition()
        self.st.SetLabel("Current mouse pos: " + str(mx) + ", " + str(my))
        wx.CallLater(20, self.captureMousePos)
        return (mx, my)

if __name__ == '__main__':
    app = wx.App()
    frm = CoordsFrame(None, title='Screen Coordinate Helper')
    frm.Show()
    app.MainLoop()

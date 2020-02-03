# ScreenCoordinateHelper
Use this to find screen coordinates by pointing to them with your mouse. Also can be used to calculate bounding boxes.

It uses the "Hello World" example from wxPython as a base and is real ugly - but it gets the job done.

When the application window is open, the coordinates currently pointed to by the mouse on your screen will be shown.

![Application in use](/screenshots/application.PNG?raw=true)

If you want to find details about a particular bounding-box, pressing space will lock this coordinate, allowing you to point to another location on the screen and press space again.
This will show you the coordinates of both points on the screen as well as the width/height of the box formed by them.

![Box details](/screenshots/box.png?raw=true)

## Usage from Source
1) Use pip to grab wxPython (see requirements.txt)
2) python coords.py

## Usage from Binary
Run the exe file from the Releases section..!

## Building the Binary
I used pyinstaller like so:
    pyinstaller .\coords.py --onefile --noconsole

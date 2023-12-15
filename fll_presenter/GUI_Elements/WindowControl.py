import pywinctl

def getWindowTitles():                      # For Score Swapper
    return pywinctl.getAllAppsWindowsTitles()

def getWindowExecutableNames():             # For Music Picker
    return pywinctl.getAllAppsNames()

def toggleWindow(window):
    window = pywinctl.getWindowsWithTitle(window)[0]
    if (window.isVisible):
        window.hide()
    else:
        window.show()
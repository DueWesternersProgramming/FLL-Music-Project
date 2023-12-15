"""Module to control window hiding and name retrieval"""
import pywinctl

def get_window_executable_names():
    """Function to return executable names for the music picker"""
    return pywinctl.getAllAppsNames()

def toggle_window(window):
    """Function to toggle hiding the window with the entered name"""
    window = pywinctl.getWindowsWithTitle(window)[0]
    if window.isVisible:
        window.hide()
    else:
        window.show()

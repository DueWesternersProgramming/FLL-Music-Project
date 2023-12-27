"""Module to control window hiding and name retrieval"""
import pywinctl

WINDOW = None

def get_window_executable_names():
    """Function to return executable names for the music picker"""
    return pywinctl.getAllAppsNames()

def define_window(window):
    """Function attempts to set the global WINDOW variable"""
    global WINDOW
    try:
        WINDOW = pywinctl.getWindowsWithTitle(window)[0]
    except IndexError:
        print(window + ": Window currently hidden or unavailable")

def toggle_window(my_window):
    """Function to toggle hiding the window with the entered name"""
    global WINDOW
    define_window(my_window)
    if WINDOW.isVisible:
        WINDOW.hide()
    else:
        WINDOW.show()

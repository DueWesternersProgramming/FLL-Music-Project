"""Module to control window hiding and name retrieval"""
import pywinctl

WINDOW = None

def get_window_executable_names():
    """Function to return executable names for the music picker"""
    return pywinctl.getAllAppsNames()

def toggle_window(my_window):
    """Function to toggle hiding the window with the entered name"""
    global WINDOW
    try:
        WINDOW = pywinctl.getWindowsWithTitle(my_window)[0]
    except Exception:
        print(my_window + ": Window currently hidden or unavailable")
    if WINDOW.isVisible:
        WINDOW.hide()
    else:
        WINDOW.show()

"""Module to control window hiding and name retrieval"""
import pywinctl
from .. import shared_functions as sf

WINDOW = None

def get_window_executable_names():
    """Function to return executable names for the music picker"""
    try:
        return pywinctl.getAllAppsNames()
    except Exception as e:
        sf.report_error("Error in window_control.py "
                        + "get_window_executable_names()", e)

def define_window(window):
    """Function attempts to set the global WINDOW variable"""
    global WINDOW
    try:
        WINDOW = pywinctl.getWindowsWithTitle(window)[0]
    except IndexError:
        print(window + ": Window currently hidden or unavailable")

def toggle_window(my_window):
    """Function to toggle hiding the window with the entered name"""
    try:
        global WINDOW
        define_window(my_window)
        if WINDOW.isVisible:
            WINDOW.hide()
        else:
            WINDOW.show()
    except AttributeError as e:
        sf.report_error("Error in window_control.py toggle_window()\n"
                        + my_window, e)

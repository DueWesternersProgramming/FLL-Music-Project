"""The module that creates and runs the gui"""
import tkinter
import tkinter.colorchooser
import platform
import customtkinter as ct
from ..GUI_Elements import volume_control as vm
from ..GUI_Elements import window_control as wc
import GUI.shared_functions as shared_functions
from ..window_creation import controller_window,timer_window
system = platform.system()

def run_gui(orientation):
    """Function creates the music gui and buttons as well as starting the event loop"""
    controller_window.new_controller_window(orientation,timer_options=False,music_options=True)
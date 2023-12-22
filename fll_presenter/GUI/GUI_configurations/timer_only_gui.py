"""The module that creates and runs the gui"""
import tkinter
import tkinter.colorchooser
import platform
import customtkinter as ct
from ..GUI_Elements import window_control as wc
from ..GUI_Elements import timer as Timer
import GUI.shared_functions as shared_functions
from ..window_creation import controller_window,timer_window

system = platform.system()
SCREENTOGGLE = False

def run_gui(orientation):
    """Function creates the timer gui and buttons as well as starting the event loop"""
    timer_window.new_timer_window()
    controller_window.new_controller_window(orientation,music_options=False,timer_options=True)

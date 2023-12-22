"""The module that creates and runs the gui"""
import tkinter
import tkinter.colorchooser
import platform
import sys
import time
import customtkinter as ct
from ..GUI_Elements import volume_control as vm
from ..GUI_Elements import window_control as wc
from ..GUI_Elements import timer as Timer
import GUI.shared_functions as shared_functions
from ..window_creation import controller_window,timer_window

system = platform.system()
LASTCLICKMS = 0
CLICKCOOLDOWN = 5           # Volume Control Cooldown In Seconds
SCREENTOGGLE = False

def run_gui(orientation):
    """Function creates the main gui and buttons as well as starting the event loop"""
    timer_window.new_timer_window()
    controller_window.new_controller_window(orientation, timer_options=True, music_options=True)
    
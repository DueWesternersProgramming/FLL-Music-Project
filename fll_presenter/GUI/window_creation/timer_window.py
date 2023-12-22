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

system = platform.system()
LASTCLICKMS = 0
CLICKCOOLDOWN = 5           # Volume Control Cooldown In Seconds
SCREENTOGGLE = False
global timer

def new_timer_window():
    """Function creates the main gui and buttons as well as starting the event loop"""
    timer_window = tkinter.Tk()
    timer_window.geometry("400x350")
    timer_window.title("Timer Window")
    timer_window.configure(background="#242424")

    timer = ct.CTkLabel(timer_window,text="2:30",text_color="#dce4ee")
    timer.configure(font=("Helvetica", 200))
    timer.place(relx=.5, rely=.5,anchor="c")
    timer_window.protocol("WM_DELETE_WINDOW", lambda:shared_functions.kill_windows(timer_window,controller))

def set_timer_size(scale):
    """Function to update the size of the Timer widget"""
    Timer.update_size(timer,scale)
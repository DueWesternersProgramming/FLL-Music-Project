import tkinter
import tkinter.colorchooser
import platform
import customtkinter as ct
from ..GUI_Elements import timer as Timer_Element

system = platform.system()
LASTCLICKMS = 0
CLICKCOOLDOWN = 5           # Volume Control Cooldown In Seconds
SCREENTOGGLE = False
global timer

def new_timer_window():
    """Function creates the main gui and buttons as well as starting the event loop"""
    global timer
    timer_window = tkinter.Tk()
    timer_window.geometry("400x350")
    timer_window.title("Timer Window")
    timer_window.configure(background="#242424")

    timer = ct.CTkLabel(timer_window,text="2:30",text_color="#dce4ee")
    timer.configure(font=("Helvetica", 200))
    timer.place(relx=.5, rely=.5,anchor="c")
    return timer_window

def set_timer_size(scale):
    """Function to update the size of the Timer widget"""
    Timer_Element.update_size(timer,scale)
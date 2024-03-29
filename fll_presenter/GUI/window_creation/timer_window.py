"""The module that creates and returns a timer window"""
import tkinter
import tkinter.colorchooser
import customtkinter as ct
from ..GUI_Elements import timer as Timer_Element

TIMER = None

def new_timer_window():
    """Function creates the timer window"""
    global TIMER
    timer_window = tkinter.Tk()
    timer_window.geometry("400x350")
    timer_window.title("Timer Window")
    timer_window.configure(background="#242424")

    TIMER = ct.CTkLabel(timer_window,text="2:30",text_color="#dce4ee")
    TIMER.configure(font=("Helvetica", 200))
    TIMER.place(relx=.5, rely=.5,anchor="c")
    return timer_window

def set_timer_size(scale):
    """Function to update the size of the Timer widget"""
    Timer_Element.update_size(TIMER,scale)

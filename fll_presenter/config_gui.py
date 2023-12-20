"""The module that creates and runs a configuration gui"""
import platform
import customtkinter as ct
from GUI_configurations import main_gui
import GUI_configurations.music_only_gui as music_gui
import GUI_configurations.timer_only_gui as timer_gui

system = platform.system()
CONFIGWINDOW = None

def run_gui():
    """Function creates the config gui and buttons as well as starting the event loop"""

    global CONFIGWINDOW
    CONFIGWINDOW = ct.CTk()
    CONFIGWINDOW.wm_geometry("400x150")
    CONFIGWINDOW.wm_title("FLL Presenter")
    ct.set_appearance_mode("dark")

    full_gui = ct.CTkButton(CONFIGWINDOW,text="Full Options",
    command=lambda win = CONFIGWINDOW:open_full_gui(win), font=("Serif", 30))
    full_gui.pack(side="top",fill="x")

    timer_only_gui = ct.CTkButton(CONFIGWINDOW,text="Timer Control Only",
    command=lambda win = CONFIGWINDOW:open_timer_gui(win), font=("Serif", 30))
    timer_only_gui.pack(side="top",fill="x")

    music_only_gui = ct.CTkButton(CONFIGWINDOW,text="Music Control Only",
    command=lambda win = CONFIGWINDOW:open_music_gui(win), font=("Serif", 30))
    music_only_gui.pack(side="top",fill="x")

    CONFIGWINDOW.protocol("WM_DELETE_WINDOW",
    lambda window=CONFIGWINDOW: main_gui.kill_windows(window))
    CONFIGWINDOW.mainloop()

def open_full_gui(window):
    """Function to open the full gui"""
    window.destroy()
    main_gui.run_gui()

def open_music_gui(window):
    """Function to open the music gui"""
    window.destroy()
    music_gui.run_gui()


def open_timer_gui(window):
    """Function to open the timer gui"""
    window.destroy()
    timer_gui.run_gui()
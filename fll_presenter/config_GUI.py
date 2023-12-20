"""The module that creates and runs the gui"""
import tkinter
import platform
import time
import customtkinter as ct
import GUI_configurations.main_gui as main_gui
import GUI_configurations.music_only_gui as music_gui
import GUI_configurations.timer_only_gui as timer_gui

system = platform.system()

def run_gui():
    """Function creates the config gui and buttons as well as starting the event loop"""


    global config_window
    config_window = ct.CTk()
    config_window.wm_geometry("400x350")
    config_window.wm_title("Timer Window")
    ct.set_appearance_mode("dark")

    full_gui = ct.CTkButton(config_window,text="Full options",command=lambda win = config_window:open_full_gui(win))
    full_gui.pack(side="top",fill="x")

    timer_only_gui = ct.CTkButton(config_window,text="Timer control only",command=lambda win = config_window:open_timer_gui(win))
    timer_only_gui.pack(side="top",fill="x")

    music_only_gui = ct.CTkButton(config_window,text="Music control only",command=lambda win = config_window:open_music_gui(win))
    music_only_gui.pack(side="top",fill="x")

    config_window.protocol("WM_DELETE_WINDOW", lambda window=config_window: main_gui.kill_windows(window))
    config_window.mainloop()

def open_full_gui(window):
    window.destroy()
    main_gui.run_gui()

def open_music_gui(window):
    window.destroy()
    music_gui.run_gui()


def open_timer_gui(window):
    window.destroy()
    timer_gui.run_gui()


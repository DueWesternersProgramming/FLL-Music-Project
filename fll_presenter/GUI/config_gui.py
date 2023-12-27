"""The module that creates and runs a configuration gui"""
import platform
import sys
import customtkinter as ct
from . import shared_functions
from .window_creation import controller_window as controller_window_module
from .window_creation import timer_window as timer_window_module

system = platform.system()
CONFIGWINDOW = None

def run_gui():
    """Function creates the config gui and buttons as well as starting the event loop"""
    global CONFIGWINDOW
    CONFIGWINDOW = ct.CTk()
    CONFIGWINDOW.wm_geometry("400x175")
    CONFIGWINDOW.wm_title("FLL Presenter")
    ct.set_appearance_mode("dark")

    def open_full_gui(window):
        """Function to open the full gui"""
        window.destroy()
        timer_window = timer_window_module.new_timer_window()
        controller_window = controller_window_module.new_controller_window(switch.get(),
        timer_options=True, music_options=True, timer=timer_window_module.TIMER,
        timer_window=timer_window)
        timer_window.protocol("WM_DELETE_WINDOW",
        lambda:shared_functions.kill_windows(timer_window,controller_window))
        controller_window.protocol("WM_DELETE_WINDOW",
        lambda:shared_functions.kill_windows(controller_window,timer_window))


    def open_music_gui(window):
        """Function to open the music gui"""
        window.destroy()
        controller_window = controller_window_module.new_controller_window(switch.get(),
        timer_options=False, music_options=True)
        controller_window.protocol("WM_DELETE_WINDOW",
        lambda:shared_functions.kill_windows(controller_window))

    def open_timer_gui(window):
        """Function to open the timer gui"""
        window.destroy()
        timer_window = timer_window_module.new_timer_window()
        controller_window = controller_window_module.new_controller_window(switch.get(),
        music_options=False, timer_options=True, timer=timer_window_module.TIMER,
        timer_window=timer_window)
        timer_window.protocol("WM_DELETE_WINDOW",
        lambda:shared_functions.kill_windows(timer_window,controller_window))
        controller_window.protocol("WM_DELETE_WINDOW",
        lambda:shared_functions.kill_windows(controller_window,timer_window))

    full_gui = ct.CTkButton(CONFIGWINDOW,text="Full Options",
    command=lambda win = CONFIGWINDOW:open_full_gui(win), font=("Serif", 30))
    full_gui.pack(side="top",fill="x")

    timer_only_gui = ct.CTkButton(CONFIGWINDOW,text="Timer Control Only",
    command=lambda win = CONFIGWINDOW:open_timer_gui(win), font=("Serif", 30))
    timer_only_gui.pack(side="top",fill="x")

    music_only_gui = ct.CTkButton(CONFIGWINDOW,text="Music Control Only",
    command=lambda win = CONFIGWINDOW:open_music_gui(win), font=("Serif", 30))
    music_only_gui.pack(side="top",fill="x")

    switch = ct.CTkSwitch(CONFIGWINDOW, text="Vertical Arangement")
    switch.pack(side="top")

    CONFIGWINDOW.protocol("WM_DELETE_WINDOW", lambda:sys.exit())
    CONFIGWINDOW.mainloop()

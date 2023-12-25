"""The module that creates and runs a configuration gui"""
import platform
import sys
import customtkinter as ct
from . import shared_functions
from .window_creation import controller_window
from .window_creation import timer_window

system = platform.system()
CONFIGWINDOW = None
CONTROLLERWINDOW = None
TIMERWINDOW = None

def run_gui():
    """Function creates the config gui and buttons as well as starting the event loop"""
    global CONFIGWINDOW, CONTROLLERWINDOW, TIMERWINDOW
    CONFIGWINDOW = ct.CTk()
    CONFIGWINDOW.wm_geometry("400x175")
    CONFIGWINDOW.wm_title("FLL Presenter")
    ct.set_appearance_mode("dark")

    def open_full_gui(window):
        """Function to open the full gui"""
        global CONTROLLERWINDOW, TIMERWINDOW
        window.destroy()
        TIMERWINDOW = timer_window.new_timer_window()
        CONTROLLERWINDOW = controller_window.new_controller_window(switch.get(), timer_options=True,
        music_options=True, timer=timer_window.TIMER, timer_window=TIMERWINDOW)
        TIMERWINDOW.protocol("WM_DELETE_WINDOW",
        lambda:shared_functions.kill_windows(TIMERWINDOW,CONTROLLERWINDOW))
        CONTROLLERWINDOW.protocol("WM_DELETE_WINDOW",
        lambda:shared_functions.kill_windows(CONTROLLERWINDOW,TIMERWINDOW))


    def open_music_gui(window):
        """Function to open the music gui"""
        global CONTROLLERWINDOW
        window.destroy()
        CONTROLLERWINDOW = controller_window.new_controller_window(switch.get(),
        timer_options=False, music_options=True)
        CONTROLLERWINDOW.protocol("WM_DELETE_WINDOW",
        lambda:shared_functions.kill_windows(CONTROLLERWINDOW,TIMERWINDOW))

    def open_timer_gui(window):
        """Function to open the timer gui"""
        global CONTROLLERWINDOW, TIMERWINDOW
        window.destroy()
        TIMERWINDOW = timer_window.new_timer_window()
        CONTROLLERWINDOW = controller_window.new_controller_window(switch.get(),
        music_options=False, timer_options=True, timer=timer_window.TIMER, timer_window=TIMERWINDOW)
        TIMERWINDOW.protocol("WM_DELETE_WINDOW",
        lambda:shared_functions.kill_windows(TIMERWINDOW,CONTROLLERWINDOW))
        CONTROLLERWINDOW.protocol("WM_DELETE_WINDOW",
        lambda:shared_functions.kill_windows(CONTROLLERWINDOW,TIMERWINDOW))

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

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

system = platform.system()
LASTCLICKMS = 0
CLICKCOOLDOWN = 5           # Volume Control Cooldown In Seconds
SCREENTOGGLE = False

def run_gui(orientation):
    """Function creates the main gui and buttons as well as starting the event loop"""
    if orientation == 0:
        pack_var = "left"
        second_pack_var = "right"
        fill_var = "y"
        controller_size = "1325x250"
        
    elif orientation == 1:
        pack_var = "top"
        second_pack_var = "bottom"
        fill_var = "x"
        controller_size = "250x600"

    controller = tkinter.Tk()
    controller.title("Controller Window")
    controller.geometry(controller_size)
    controller.configure(background='#242424')

    timer_window = tkinter.Tk()
    timer_window.geometry("400x350")
    timer_window.title("Timer Window")
    timer_window.configure(background="#242424")

    timer = ct.CTkLabel(timer_window,text="2:30",text_color="#dce4ee")
    timer.configure(font=("Helvetica", 200))
    timer.place(relx=.5, rely=.5,anchor="c")

    toggle_full_screen_button = ct.CTkButton(controller, text="Toggle\nFull\nScreen",
    command=lambda:shared_functions.toggle_full_screen(timer_window),
    width=110, height= 3, font=("Serif", 20))
    toggle_full_screen_button.pack(side=second_pack_var, fill=fill_var)

    update_color_button = ct.CTkButton(controller, text="Change\nTimer\nBackground",
    command=lambda: timer_window.configure(background=str(shared_functions.open_color_menu(timer_window))),
    width=110, height= 3, font=("Serif", 20))
    update_color_button.pack(side=second_pack_var, fill=fill_var)

    start_timer_button = ct.CTkButton(controller, text="Start Timer",
    command=lambda: Timer.start_timer(timer),
    width=110, height= 3, font=("Serif", 20))

    stop_timer_button = ct.CTkButton(controller, text="Stop Timer",
    command=lambda: Timer.stop_timer(timer),
    width=110, height=3, font=("Serif", 20))

    timer_toggle_button = ct.CTkButton(controller, text="Hide/Show Timer",
    command=lambda: wc.toggle_window("Timer Window"),
    width=110, height=3, font=("Serif", 20))

    volume_up_button = ct.CTkButton(controller, text="Volume Up",
    command=lambda: shared_functions.call_volume_control(True, controller, system),
    width=110, height=3, font=("Serif", 20))

    volume_down_button = ct.CTkButton(controller, text="Volume Down",
    command=lambda: shared_functions.call_volume_control(False, controller, system),
    width=110, height=3, font=("Serif", 20))

    min_volume_slider = ct.CTkSlider(controller, width=20, from_=0, to=100,
    number_of_steps=100, orientation="vertical", command=shared_functions.set_volume_minimum)
    min_volume_slider.set(vm.get_volume_control()[0])

    max_volume_slider = ct.CTkSlider(controller, width=20, from_=0, to=100,
    number_of_steps=100, orientation="vertical", command=shared_functions.set_volume_maximum)
    max_volume_slider.set(vm.get_volume_control()[1])


    start_timer_button.pack(side=(pack_var), fill=fill_var)
    stop_timer_button.pack(side=(pack_var), fill=fill_var)
    timer_toggle_button.pack(side=(pack_var), fill=fill_var)
    volume_up_button.pack(side=(pack_var), fill=fill_var)
    volume_down_button.pack(side=(pack_var), fill=fill_var)
    min_volume_slider.pack(side=("left"), fill="y")
    max_volume_slider.pack(side=("left"), fill="y")

    def set_timer_size(scale):
        """Function to update the size of the Timer widget"""
        Timer.update_size(timer,scale)

    if system == "Windows":
        application_selector = ct.CTkOptionMenu(controller, values=wc.get_window_executable_names(),
        command=shared_functions.set_audio_application)
        application_selector.pack(side="left")
        application_selector.after(10000,
        lambda:shared_functions.schedule_dropdown_update(controller, application_selector))

    timer_size = ct.CTkSlider(controller, width=20, from_=0, to=1000,
    orientation="vertical")
    timer_size.configure(command=set_timer_size)
    timer_size.set(200)
    timer_size.pack(side=("left"), fill="y")

    timer_window.protocol("WM_DELETE_WINDOW", lambda:shared_functions.kill_windows(controller,timer_window))
    controller.protocol("WM_DELETE_WINDOW", lambda:shared_functions.kill_windows(controller,timer_window))

    timer_window.mainloop()
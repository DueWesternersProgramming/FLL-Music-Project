"""The module that creates and returns a controller window"""
import tkinter
import tkinter.colorchooser
import platform
import customtkinter as ct
from GUI import shared_functions
from ..GUI_Elements import volume_control as vm
from ..GUI_Elements import window_control as wc
from ..GUI_Elements import timer as Timer_Element

system = platform.system()

def new_controller_window(orientation,music_options=True,timer_options=True,
                          timer=None,timer_window=None):
    """Function creates the main gui and buttons as well as starting the event loop"""
    if orientation == 0:
        pack_var = "left"
        second_pack_var = "right"
        if music_options and not timer_options:
            controller_size = "525x250"
        elif timer_options and not music_options:
            controller_size = "785x250"
        else:
            controller_size = "1315x250"

    elif orientation == 1:
        pack_var = "top"
        second_pack_var = "bottom"
        if music_options and not timer_options:
            controller_size = "250x300"
        elif timer_options and not music_options:
            controller_size = "250x500"
        else:
            controller_size = "250x600"

    controller = tkinter.Tk()
    controller.title("Controller Window")
    controller.geometry(controller_size)
    controller.configure(background='#242424')

    if timer_options:
        def set_timer_size(scale):
            """Function to update the size of the Timer widget"""
            Timer_Element.update_size(timer,scale)

        toggle_full_screen_button = ct.CTkButton(controller, text="Toggle\nFull\nScreen",
        command=lambda:shared_functions.toggle_full_screen(timer_window),
        width=110, height= 3, font=("Serif", 20))
        toggle_full_screen_button.pack(side=second_pack_var, fill="both", expand=True)

        update_color_button = ct.CTkButton(controller, text="Change\nTimer\nBackground",
        command=lambda: timer_window.configure(background=
        str(shared_functions.open_color_menu(timer_window))),
        width=115, height= 3, font=("Serif", 20))
        update_color_button.pack(side=second_pack_var, fill="both", expand=True)

        start_timer_button = ct.CTkButton(controller, text="Start Timer",
        command=lambda: Timer_Element.start_timer(timer), width=110, height= 3, font=("Serif", 20))

        stop_timer_button = ct.CTkButton(controller, text="Stop Timer",
        command=lambda: Timer_Element.stop_timer(timer), width=110, height=3, font=("Serif", 20))

        timer_toggle_button = ct.CTkButton(controller, text="Hide/Show Timer",
        width=110, height=3, font=("Serif", 20))
        timer_toggle_button._command = lambda: shared_functions.toggle_window("Timer Window",
        timer_toggle_button)

        start_timer_button.pack(side=pack_var, fill="both", expand=True)
        stop_timer_button.pack(side=pack_var, fill="both", expand=True)
        timer_toggle_button.pack(side=pack_var, fill="both", expand=True)

        timer_size = ct.CTkSlider(controller, width=20, from_=0, to=1000,orientation="vertical")
        timer_size.configure(command=set_timer_size)
        timer_size.set(200)
        timer_size.after(50, lambda: timer_size.pack(side=pack_var, fill="y", expand=True))

    if music_options:
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

        volume_up_button.pack(side=pack_var, fill="both", expand=True)
        volume_down_button.pack(side=pack_var, fill="both", expand=True)
        min_volume_slider.pack(side=("left"), fill="y", expand=True)
        max_volume_slider.pack(side=("left"), fill="y", expand=True)
        if system == "Windows":
            application_selector = ct.CTkOptionMenu(controller,
            values=wc.get_window_executable_names(),
            command=shared_functions.set_audio_application)
            application_selector.pack(side="left", fill='x', expand=True)
            application_selector.after(10000,
            lambda:shared_functions.schedule_dropdown_update(controller, application_selector))

    return controller

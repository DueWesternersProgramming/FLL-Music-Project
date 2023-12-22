"""The module that creates and runs the gui"""
import tkinter
import tkinter.colorchooser
import platform
import customtkinter as ct
import GUI_Elements.volume_control as vm
import GUI_Elements.window_control as wc
import shared_functions

system = platform.system()

def run_gui(orientation):
    """Function creates the music gui and buttons as well as starting the event loop"""
    if orientation == 0:
        pack_var = "left"
        second_pack_var = "right"
        fill_var = "y"
        
    elif orientation == 1:
        pack_var = "top"
        second_pack_var = "bottom"
        fill_var = "x"

    controller = tkinter.Tk()
    controller.title("Controller Window")
    controller.geometry("500x250")
    controller.configure(background='#242424')

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

    volume_up_button.pack(side=(pack_var), fill=fill_var)
    volume_down_button.pack(side=(pack_var), fill=fill_var)
    min_volume_slider.pack(side=(pack_var), fill='y')
    max_volume_slider.pack(side=(pack_var), fill='y')

    if system == "Windows":
        application_selector = ct.CTkOptionMenu(controller, values=wc.get_window_executable_names(),
        command=shared_functions.set_audio_application)
        application_selector.pack(side=pack_var)
        application_selector.after(10000,
        lambda:shared_functions.schedule_dropdown_update(controller, application_selector))

    controller.protocol("WM_DELETE_WINDOW", lambda:shared_functions.kill_windows(controller))

    controller.mainloop()

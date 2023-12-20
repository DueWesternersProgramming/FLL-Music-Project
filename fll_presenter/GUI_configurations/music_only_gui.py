"""The module that creates and runs the gui"""
import tkinter
import tkinter.colorchooser
import platform
import time
import customtkinter as ct
import GUI_Elements.volume_control as vm
import GUI_Elements.window_control as wc
import GUI_Elements.timer as Timer
import GUI_configurations.main_gui as main_gui


system = platform.system()
LASTCLICKMS = 0
CLICKCOOLDOWN = 5           # Volume Control Cooldown In Seconds
SCREENTOGGLE = False

def run_gui():
    """Function creates the main gui and buttons as well as starting the event loop"""


    #timer_window.bind("<F11>", lambda:timer_window.attributes("-fullscreen", True))
    #timer_window.bind("<Escape>", lambda:timer_window.attributes("-fullscreen", False))

    controller = tkinter.Tk()
    controller.title("Controller Window")
    controller.geometry("1325x250")
    controller.configure(background='#242424')


    volume_up_button = ct.CTkButton(controller, text="Volume Up",
    command=lambda: main_gui.call_volume_control(True, controller, system),
    width=110, height=3, font=("Serif", 20))

    volume_down_button = ct.CTkButton(controller, text="Volume Down",
    command=lambda: main_gui.call_volume_control(False, controller, system),
    width=110, height=3, font=("Serif", 20))

    min_volume_slider = ct.CTkSlider(controller, width=20, from_=0, to=100,
    number_of_steps=100, orientation="vertical", command=main_gui.set_volume_minimum)
    min_volume_slider.set(vm.get_volume_control()[0])

    max_volume_slider = ct.CTkSlider(controller, width=20, from_=0, to=100,
    number_of_steps=100, orientation="vertical", command=main_gui.set_volume_maximum)
    max_volume_slider.set(vm.get_volume_control()[1])

    volume_up_button.pack(side=("left"), fill='y')
    volume_down_button.pack(side=("left"), fill='y')
    min_volume_slider.pack(side=("left"), fill='y')
    max_volume_slider.pack(side=("left"), fill='y')



    if system == "Windows":
        application_selector = ct.CTkOptionMenu(controller, values=wc.get_window_executable_names(),
        command=main_gui.set_audio_application)
        application_selector.pack(side="left")
        application_selector.after(10000,
        lambda:main_gui.schedule_dropdown_update(controller, application_selector))


    controller.protocol("WM_DELETE_WINDOW", lambda:main_gui.kill_windows(controller))

    controller.mainloop()


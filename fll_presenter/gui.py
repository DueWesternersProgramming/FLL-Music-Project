"""The module that creates and runs the gui"""
import tkinter
import platform
import time
import customtkinter as ct
import GUI_Elements.volume_control as vm
import GUI_Elements.window_control as wc
import GUI_Elements.timer as Timer

system = platform.system()
LASTCLICKMS = 0
CLICKCOOLDOWN = 5           # Volume Control Cooldown In Seconds

def run_gui():
    """Function creates the main gui and buttons as well as starting the event loop"""
    timer_window = ct.CTk()
    timer_window.geometry("400x350")
    timer_window.title("Timer Window")
    ct.set_appearance_mode("dark")
    #timer_window.bind("<F11>", lambda:timer_window.attributes("-fullscreen", True))
    #timer_window.bind("<Escape>", lambda:timer_window.attributes("-fullscreen", False))

    controller = tkinter.Tk()
    controller.title("Controller Window")
    controller.geometry("900x250")
    controller.configure(background='#242424')

    start_timer_button = ct.CTkButton(controller, text="Start Timer",
    command=lambda: Timer.start_timer(timer),
    width=110, height= 3, font=("Serif", 20))

    stop_timer_button = ct.CTkButton(controller, text="Stop Timer",
    command=lambda: Timer.stop_timer(timer),
    width=110, height=3, font=("Serif", 20))

    timer_toggle_button = ct.CTkButton(controller, text="Hide Timer",
    command=lambda: wc.toggle_window("Timer Window"),
    width=110, height=3, font=("Serif", 20))

    volume_up_button = ct.CTkButton(controller, text="Volume Up",
    command=lambda: call_volume_control(True, controller, system),
    width=110, height=3, font=("Serif", 20))

    volume_down_button = ct.CTkButton(controller, text="Volume Down",
    command=lambda: call_volume_control(False, controller, system),
    width=110, height=3, font=("Serif", 20))

    min_volume_slider = ct.CTkSlider(controller, width=20, from_=0, to=100,
    number_of_steps=100, orientation="vertical", command=set_volume_minimum)
    min_volume_slider.set(vm.get_volume_control()[0])

    max_volume_slider = ct.CTkSlider(controller, width=20, from_=0, to=100,
    number_of_steps=100, orientation="vertical", command=set_volume_maximum)
    max_volume_slider.set(vm.get_volume_control()[1])

    start_timer_button.pack(side=("left"), fill='y')
    stop_timer_button.pack(side=("left"), fill='y')
    timer_toggle_button.pack(side=("left"), fill='y')
    volume_up_button.pack(side=("left"), fill='y')
    volume_down_button.pack(side=("left"), fill='y')
    min_volume_slider.pack(side=("left"), fill='y')
    max_volume_slider.pack(side=("left"), fill='y')

    if system == "Windows":
        application_selector = ct.CTkOptionMenu(controller, values=wc.get_window_executable_names(),
        command=set_audio_application)
        application_selector.pack(side="left")

    timer = ct.CTkLabel(timer_window,text="2:30")
    timer.configure(font=("Serif", 700))
    timer.pack(fill='x')
    #timer.place(relx=.5, rely=.5,anchor="s")

    timer_window.mainloop()    

def call_volume_control(option, controller, os):
    """Function to call volume control with a 1 second cooldown"""
    global LASTCLICKMS
    if time.time() > (LASTCLICKMS + CLICKCOOLDOWN):
        vm.volume_control(option, controller, os)
        LASTCLICKMS = time.time()

def set_volume_minimum(min_volume):
    """Function to send the new volume minimum"""
    vm.set_volume_control(min_volume, vm.get_volume_control()[1])

def set_volume_maximum(max_volume):
    """Function to send the new volume maximum"""
    vm.set_volume_control(vm.get_volume_control()[0], max_volume)

def set_audio_application(application):
    """Function to send the new audio application"""
    vm.set_volume_application(application)
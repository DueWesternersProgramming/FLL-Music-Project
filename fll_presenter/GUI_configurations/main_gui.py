"""The module that creates and runs the gui"""
import tkinter
import tkinter.colorchooser
import platform
import sys
import time
import customtkinter as ct
import GUI_Elements.volume_control as vm
import GUI_Elements.window_control as wc
import GUI_Elements.timer as Timer


system = platform.system()
LASTCLICKMS = 0
CLICKCOOLDOWN = 5           # Volume Control Cooldown In Seconds
SCREENTOGGLE = False

def run_gui():
    """Function creates the main gui and buttons as well as starting the event loop"""
    controller = tkinter.Tk()
    controller.title("Controller Window")
    controller.geometry("1325x250")
    controller.configure(background='#242424')

    timer_window = tkinter.Tk()
    timer_window.geometry("400x350")
    timer_window.title("Timer Window")
    timer_window.configure(background="#242424")

    timer = ct.CTkLabel(timer_window,text="2:30",text_color="#dce4ee")
    timer.configure(font=("Helvetica", 200))
    timer.place(relx=.5, rely=.5,anchor="c")

    toggle_full_screen_button = ct.CTkButton(controller, text="Toggle\nFull\nScreen",
    command=lambda:toggle_full_screen(timer_window),
    width=110, height= 3, font=("Serif", 20))
    toggle_full_screen_button.pack(side="right", fill="y")

    update_color_button = ct.CTkButton(controller, text="Change\nTimer\nBackground",
    command=lambda: timer_window.configure(background=str(open_color_menu(timer_window))),
    width=110, height= 3, font=("Serif", 20))
    update_color_button.pack(side="right", fill="y")

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


    def set_timer_size(scale):
        """Function to update the size of the Timer widget"""
        Timer.update_size(timer,scale)

    if system == "Windows":
        application_selector = ct.CTkOptionMenu(controller, values=wc.get_window_executable_names(),
        command=set_audio_application)
        application_selector.pack(side="left")
        application_selector.after(10000,
        lambda:schedule_dropdown_update(controller, application_selector))

    timer_size = ct.CTkSlider(controller, width=20, from_=0, to=1000,
    orientation="vertical")
    timer_size.configure(command=set_timer_size)
    timer_size.set(200)
    timer_size.pack(side=("right"), fill='y')

    timer_window.protocol("WM_DELETE_WINDOW", lambda:kill_windows(controller,timer_window))
    controller.protocol("WM_DELETE_WINDOW", lambda:kill_windows(controller,timer_window))

    timer_window.mainloop()


def schedule_dropdown_update(window, selector):
    """Function to update the selector applications"""
    selector.configure(values=wc.get_window_executable_names())
    window.update()
    selector.after(10000, lambda: schedule_dropdown_update(window, selector))


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

def kill_windows(controller, timer_window = None, kill_program = True):
    """Function to kill the tkinter fll_presenter windows and exit the program"""
    print("KILLING PROGRAM/WINDOW(S)")
    controller.destroy()
    if timer_window is not None:
        timer_window.destroy()
    if kill_program is True:
        sys.exit()

def open_color_menu(timer_window):
    """Function to open a new color selector window for the color of the timer window"""
    color = tkinter.colorchooser.askcolor(
    title="Select a new color for the background of the display",
                        initialcolor=timer_window['background'])[1]
    if color is None:
        return timer_window['background']
    return color

def toggle_full_screen(window):
    """Function that uses a boolean to toggle full screen on and off for the argument window"""
    global SCREENTOGGLE
    if SCREENTOGGLE is False:
        full_screen(window)
        SCREENTOGGLE = True
    elif SCREENTOGGLE is True:
        exit_full_screen(window)
        SCREENTOGGLE = False


def full_screen(window):
    """Function that fullscreens the supplied window"""
    window.attributes("-fullscreen", True)

def exit_full_screen(window):
    """Function that exits fullscreen on the supplied window"""
    window.attributes("-fullscreen", False)
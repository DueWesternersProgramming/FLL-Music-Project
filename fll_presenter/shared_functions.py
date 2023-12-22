"""File to hold the shared functions between timer and controller windows"""
import tkinter
import tkinter.colorchooser
import platform
import sys
import time
import GUI_Elements.volume_control as vm
import GUI_Elements.window_control as wc
import GUI_Elements.timer as Timer

system = platform.system()
LASTCLICKMS = 0
CLICKCOOLDOWN = 5           # Volume Control Cooldown In Seconds
SCREENTOGGLE = False

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
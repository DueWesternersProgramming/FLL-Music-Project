"""The module that creates and returns a timer window"""

import tkinter
import tkinter.colorchooser
import customtkinter as ct
from .draggable_widget import DraggableWidget
from ..Hardware_Control_Elements import timer as Timer_Element
from ..Hardware_Control_Elements import camera_stream as cs


TIMER = None
camera_stream_widgets = []
cams = {}


def new_timer_window(has_camera_stream=False):
    """Function creates the timer window"""
    global TIMER
    global camera_stream_widgets
    global cams
    timer_window = tkinter.Tk()
    timer_window.geometry("400x350")
    timer_window.title("Timer Window")
    timer_window.configure(background="#242424")

    TIMER = ct.CTkLabel(timer_window, text="2:30", text_color="#dce4ee")
    TIMER.configure(font=("Helvetica", 200))
    TIMER.place(relx=0.5, rely=0.5, anchor="c")

    if has_camera_stream:
        cams = cs.get_avalible_cameras()

        print("Available cameras:", cams)

        if len(cams) == 0:
            return timer_window

        cs.init_cameras(list(cams.keys()))

        for i in list(cams.keys()):
            print("Creating camera stream widget", i)

            camera_stream_widgets.append(tkinter.Label(timer_window))
            camera_stream_widgets[i].place(x=200 * i, y=20)

            DraggableWidget(
                camera_stream_widgets[i]
            )  # No need to assign this to a variable, everything is configured inside the class constructor
            # ----------------------------------
        update_video_stream()

    return timer_window


def update_video_stream():
    for i in list(cams.keys()):
        photo_image = cs.get_camera_frame(i)
        camera_stream_widgets[i].photo_image = photo_image
        camera_stream_widgets[i].configure(image=photo_image)
    camera_stream_widgets[0].after(10, update_video_stream)


def set_timer_size(scale):
    """Function to update the size of the Timer widget"""
    Timer_Element.update_size(TIMER, scale)

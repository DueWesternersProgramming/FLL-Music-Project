"""The module that creates and returns a timer window"""

import tkinter
import tkinter.colorchooser
import customtkinter as ct
# Assuming the structure is correct:
from .draggable_widget import DraggableWidget
from ..Hardware_Control_Elements import timer as Timer_Element
from ..Hardware_Control_Elements import camera_stream as cs


TIMER = None
# These are lists, and we will use sequential indices (0, 1, 2, ...) to access them.
camera_stream_widgets = []
draggable_camera_widgets = []
# This holds the camera IDs mapped to names/objects.
cams = {} 


def new_timer_window(has_camera_stream=False, cams_to_use={}):
    """Function creates the timer window"""
    global TIMER
    global camera_stream_widgets
    global draggable_camera_widgets
    global cams
    
    # Clear previous widgets if the function is called again
    camera_stream_widgets = []
    draggable_camera_widgets = []

    timer_window = tkinter.Tk()
    timer_window.geometry("400x350")
    timer_window.title("Timer Window")
    timer_window.configure(background="#242424")

    TIMER = ct.CTkLabel(timer_window, text="2:30", text_color="#dce4ee")
    TIMER.configure(font=("Helvetica", 200))
    # Corrected placement to be centered on the small window
    TIMER.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    DraggableWidget(TIMER, 8)

    if has_camera_stream:
        cams = cams_to_use
        print("Available cameras:", cams)

        if len(cams) == 0:
            return timer_window

        # Get a list of camera IDs to initialize
        camera_keys = list(cams.keys())
        cs.init_cameras(camera_keys)
        
        index = 0
        default_width = 320
        default_height = 240

        for camera_key in camera_keys:
            print("Creating camera stream widget for key:", camera_key)

            widget = tkinter.Label(timer_window)
            camera_stream_widgets.append(widget)
            
            # CRITICAL FIX: Set initial width and height using place
            widget.place(
                x=200 * index, 
                y=20, 
                width=default_width, # Explicitly set size
                height=default_height
            ) 

            draggable_widget = DraggableWidget(widget)
            draggable_camera_widgets.append(draggable_widget)

            index += 1
            
        update_video_stream()

    return timer_window


def update_video_stream():
    global camera_stream_widgets
    global draggable_camera_widgets
    global cams

    camera_keys = list(cams.keys())
    
    for i in range(len(camera_keys)):
        camera_key = camera_keys[i]
        
        # 1. Retrieve the DraggableWidget instance (where the custom size is tracked)
        draggable_instance = draggable_camera_widgets[i]
        
        # 2. Retrieve the underlying tkinter.Label widget (where the image needs to be configured)
        # This widget is stored in camera_stream_widgets
        label_widget = camera_stream_widgets[i] 
        
        # --- DETERMINE FRAME SIZE ---
        
        # Prioritize the size set by the user via the DraggableWidget if available
        width = getattr(draggable_instance, 'current_width', None)
        height = getattr(draggable_instance, 'current_height', None)

        # Fallback to the size set by .place() if the widget hasn't been resized yet
        if width is None or height is None:
             # Use the actual rendered size of the Label widget
             width = label_widget.winfo_width() 
             height = label_widget.winfo_height()
        

        # --- FETCH AND APPLY FRAME ---
        
        # 3. Get the new PhotoImage frame from the camera module
        # This assumes cs.get_camera_frame returns a usable tkinter.PhotoImage object.
        photo_image = cs.get_camera_frame(camera_key, width, height) 
        
        # 4. CRITICAL: Store the reference to the PhotoImage directly on the Label
        # This prevents the Python garbage collector from destroying the image data
        # before Tkinter can display it.
        label_widget.photo_image = photo_image
        
        # 5. Configure the Label to display the new image
        label_widget.configure(image=photo_image)
    
    # Schedule the next update
    if camera_stream_widgets:
        camera_stream_widgets[0].after(10, update_video_stream)


def set_timer_size(scale):
    """Function to update the size of the Timer widget"""
    # Assuming Timer_Element.update_size handles the CTkLabel element
    Timer_Element.update_size(TIMER.widget, scale)
"""The module that creates and runs the gui"""
import tkinter
import tkinter.colorchooser
import platform
import customtkinter as ct
from ..GUI_Elements import window_control as wc
from ..GUI_Elements import timer as Timer
import GUI.shared_functions as shared_functions

system = platform.system()
SCREENTOGGLE = False

def run_gui(orientation):
    """Function creates the timer gui and buttons as well as starting the event loop"""
    if orientation == 0:
        pack_var = "left"
        second_pack_var = "right"
        fill_var = "y"
        controller_size = "785x250"

    elif orientation == 1:
        pack_var = "top"
        second_pack_var = "bottom"
        fill_var = "x"
        controller_size = "300x500"

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

    start_timer_button = ct.CTkButton(controller, text="Start Timer",
    command=lambda: Timer.start_timer(timer),
    width=110, height= 3, font=("Serif", 20))

    stop_timer_button = ct.CTkButton(controller, text="Stop Timer",
    command=lambda: Timer.stop_timer(timer),
    width=110, height=3, font=("Serif", 20))

    timer_toggle_button = ct.CTkButton(controller, text="Hide/Show Timer",
    command=lambda: wc.toggle_window("Timer Window"),
    width=110, height=3, font=("Serif", 20))
    
    update_color_button = ct.CTkButton(controller, text="Change\nTimer\nBackground",
    command=lambda: timer_window.configure(background=str(shared_functions.open_color_menu(timer_window))),
    width=115, height= 3, font=("Serif", 20))
    
    toggle_full_screen_button = ct.CTkButton(controller, text="Toggle\nFull\nScreen",
    command=lambda:shared_functions.toggle_full_screen(timer_window),
    width=110, height= 3, font=("Serif", 20))

    start_timer_button.pack(side=(pack_var), fill=fill_var)
    stop_timer_button.pack(side=(pack_var), fill=fill_var)
    timer_toggle_button.pack(side=(pack_var), fill=fill_var)
    update_color_button.pack(side=(pack_var), fill=fill_var)
    toggle_full_screen_button.pack(side=(pack_var), fill=fill_var)

    def set_timer_size(scale):
        """Function to update the size of the Timer widget"""
        Timer.update_size(timer,scale)

    timer_size = ct.CTkSlider(controller, width=20, from_=0, to=1000,
    orientation="vertical")
    timer_size.configure(command=set_timer_size)
    timer_size.set(200)
    timer_size.pack(side=(second_pack_var), fill='y')

    timer_window.protocol("WM_DELETE_WINDOW", lambda:shared_functions.kill_windows(controller,timer_window))
    controller.protocol("WM_DELETE_WINDOW", lambda:shared_functions.kill_windows(controller,timer_window))

    timer_window.mainloop()

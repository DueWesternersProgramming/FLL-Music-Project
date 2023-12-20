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
    timer_window = ct.CTk()
    timer_window.geometry("400x350")
    timer_window.title("Timer Window")
    ct.set_appearance_mode("dark")

    #timer_window.bind("<F11>", lambda:timer_window.attributes("-fullscreen", True))
    #timer_window.bind("<Escape>", lambda:timer_window.attributes("-fullscreen", False))

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
    command=lambda:main_gui.toggle_full_screen(timer_window),
    width=110, height= 3, font=("Serif", 20))
    toggle_full_screen_button.pack(side="right", fill="y")

    update_color_button = ct.CTkButton(controller, text="Change\nTimer\nBackground",
    command=lambda: timer_window.configure(background=str(main_gui.open_color_menu(timer_window))),
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

    start_timer_button.pack(side=("left"), fill='y')
    stop_timer_button.pack(side=("left"), fill='y')
    timer_toggle_button.pack(side=("left"), fill='y')



    def set_timer_size(scale):
        """Function to update the size of the Timer widget"""
        Timer.update_size(timer,scale)



    timer_size = ct.CTkSlider(controller, width=20, from_=0, to=1000,
    orientation="vertical")
    timer_size.configure(command=set_timer_size)
    timer_size.set(200)
    timer_size.pack(side=("right"), fill='y')

    timer_window.protocol("WM_DELETE_WINDOW", lambda:main_gui.kill_windows(controller,timer_window))
    controller.protocol("WM_DELETE_WINDOW", lambda:main_gui.kill_windows(controller,timer_window))

    timer_window.mainloop()



"""The module that creates and runs the gui"""
import tkinter
import platform
import customtkinter as ct
import gui_elements.volume_control as vm
import gui_elements.timer as Timer

system = platform.system()

# TODO Sliders for min and max (Check max>min), dropdown for application selector (WINDOWS ONLY)
# TODO Refresh button for application selector (WINDOWS ONLY), Hide button for timer window

def run_gui():
    """Function creates the main gui and buttons as well as starting the event loop"""
    timer_window = ct.CTk()
    timer_window.geometry("400x350")
    timer_window.title("Timer Window")
    ct.set_appearance_mode("dark")

    controller = tkinter.Tk()
    controller.title("Controller Window")
    controller.geometry("430x250")

    start_button = ct.CTkButton(controller, text="Start Timer",
    command=lambda: Timer.start_timer(timer),
    width=10, height= 3, font=("Serif", 20))

    volume_up_button = ct.CTkButton(controller, text="Volume Up",
    command=lambda: vm.volume_control(True, controller, system),
    width=10, height=3, font=("Serif", 20))

    volume_down_button = ct.CTkButton(controller, text="Volume Down",
    command=lambda: vm.volume_control(False, controller, system),
    width=10, height=3, font=("Serif", 20))

    start_button.pack(side=("left"), fill='y')
    volume_up_button.pack(side=("left"), fill='y')
    volume_down_button.pack(side=("left"), fill='y')

    timer = ct.CTkLabel(timer_window,text="2:30")
    timer.configure(font=("Serif", 180))
    timer.place(relx=.5, rely=.5,anchor="s")

  #sheet.initEntrySheet(timerWindow)
  #sheet.initDisplaySheet(controller)

  #print(sheet.getData())


    timer_window.mainloop()

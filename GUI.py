import customtkinter as ct
import volumemanagement as vm
from GUI_Elements import startTimer
import tkinter


#customtkinter.set_appearance_mode("dark")
#print(base.test())

def runGUI():
  timerWindow = ct.CTk()
  timerWindow.geometry("400x350")
  timerWindow.title("Timer Window")

  controller = tkinter.Tk()
  controller.title("Controller Window")
  controller.geometry("430x250")

  startButton = ct.CTkButton(controller, text="Start Timer",
  command=lambda: startTimer(timer, timerWindow), 
  width=10, height= 3, font=("Serif", 20))

  volumeUpButton = ct.CTkButton(controller, text="Volume Up",
  command=lambda: vm.volumeControl(True),
  width=10, height=3, font=("Serif", 20))

  volumeDownButton = ct.CTkButton(controller, text="Volume Down",
  command=lambda: vm.volumeControl(False),
  width=10, height=3, font=("Serif", 20))

  startButton.pack(side=("left"), fill='y')
  volumeUpButton.pack(side=("left"), fill='y')
  volumeDownButton.pack(side=("left"), fill='y')

  timer = ct.CTkLabel(timerWindow,text=("2:30"))
  timer.configure(font=("Serif", 180))
  timer.pack(side="top", expand=1)

  timerWindow.mainloop()
#print(timer.winfo_width())
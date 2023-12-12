import customtkinter as ct
import VolumeControl as vm
import GUI_Elements.Timer as Timer
import GUI_Elements.sheet as sheet
import tkinter

def runGUI():
  timerWindow = ct.CTk()
  timerWindow.geometry("400x350")
  timerWindow.title("Timer Window")
  ct.set_appearance_mode("dark")

  controller = tkinter.Tk()
  controller.title("Controller Window")
  controller.geometry("430x250")

  startButton = ct.CTkButton(controller, text="Start Timer",
  command=lambda: Timer.startTimer(timer), 
  width=13, height= 3, font=("Serif", 20))

  volumeUpButton = ct.CTkButton(controller, text="Volume Up",
  command=lambda: vm.volumeControl(True, controller),
  width=13, height=3, font=("Serif", 20))

  volumeDownButton = ct.CTkButton(controller, text="Volume Down",
  command=lambda: vm.volumeControl(False, controller),
  width=13, height=3, font=("Serif", 20))

  startButton.place(relx=0.5,rely=0.5)
  volumeDownButton.place(relx=0.5,rely=0.6)
  volumeUpButton.place(relx=0.5,rely=0.7)

  timer = ct.CTkLabel(timerWindow,text=("2:30"))
  timer.configure(font=("Serif", 180))
  timer.place(relx=.5, rely=.5,anchor="s")

  sheet.initEntrySheet(timerWindow)
  sheet.initDisplaySheet(controller)
  
  #print(sheet.getData())


  timerWindow.mainloop()

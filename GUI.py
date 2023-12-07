import customtkinter as ct
import time
import tkinter

#customtkinter.set_appearance_mode("dark")
#print(base.test())

timerWindow = ct.CTk()
timerWindow.geometry("300x250")
timerWindow.title("Timer Window")

controller = ct.CTk()
controller.title("Controller Window")
controller.geometry("300x250")

startButton = ct.CTkButton(controller, text="Start Timer",
command=lambda: startTimer(), 
width=10, height= 3, font=("Serif", 20))

startButton.pack(side=("left"))

timer = ct.CTkLabel(timerWindow,text=("2:30"))
timer.configure(font=("Serif", 180))
timer.pack(side="top", pady=(timerWindow.winfo_height()/2))





def startTimer():
  min = 2
  sec = 30
  countInterval = 1
  while min >= 0:
    count = str(min) + ":" + str(sec)
    if sec < 1:
      sec = 60
      min = min - 1
    sec = sec-1
    timer.configure(text=(str(count)))
    timerWindow.update()
    time.sleep(countInterval)
  time.sleep(3)
  min = 2
  sec = 30
  count = str(min) + ":" + str(sec)
  timer.configure(text=str(count))
#print(timer.winfo_width())
timerWindow.mainloop()

import tkinter
import time
#from volumemanagement import *

timerWindow = tkinter.Tk()
timerWindow.geometry("300x250")
timerWindow.title("Timer Window")

controller = tkinter.Tk()
controller.title("Controller Window")
controller.geometry("300x250")
controller.config(bg="grey")


startButton = tkinter.Button(controller, text="Start Timer", command=lambda: startTimer(), width=10, height= 3, bg="blue", font=("Serif", 20))

x = tkinter.Label(text=("2:30"))
x.config(font=("Serif", 120))
x.pack()

x.place(
    x=timerWindow.winfo_screenwidth() / 2-115, #Offset b/c of font size.
    y=timerWindow.winfo_screenheight() / 2 - 200  #Offset b/c of font size.
)

startButton.place(
    x = (timerWindow.winfo_screenwidth()/2)-80,
    y = (timerWindow.winfo_screenheight()/2)-160
)

def startTimer():
  min = 2
  sec = 30
  interval = 1
  while min >= 0:
    count = str(min) + ":" + str(sec)
    if sec < 1:
      sec = 60
      min = min - 1
    sec = sec-1
    x.config(text=(str(count)))
    timerWindow.update()
    time.sleep(interval)
  time.sleep(3)
  min = 2
  sec = 30
  count = str(min) + ":" + str(sec)
  x.config(text=str(count))
print(x.winfo_width())
timerWindow.mainloop()

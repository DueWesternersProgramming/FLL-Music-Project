import time

def startTimer(timer, timerWindow):
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
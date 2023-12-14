import time

masterMin = 2
masterSec = 30

tickInterval = 50       # ms
resetInterval = 5000    # ms

interrupt = False
running = False

def currentTimeMillis():
  return float(round(time.time()*1000))

def startTimer(timer):
  global running, interrupt
  if running:
    stopTimer(timer)
    timer.after(tickInterval, lambda: startTimer(timer))
    return
  interrupt = False
  running = True
  timer.configure(text=str(masterMin) + ":" + str(masterSec))
  milliGoal = ((masterMin*60+masterSec)*1000)+currentTimeMillis()+1000
  timer.after(tickInterval, lambda: tick(timer, milliGoal))
    
def stopTimer(timer):
  global interrupt; interrupt = True
  timer.configure(text=str(masterMin) + ":" + str(masterSec))

def tick(timer, goal):
  global running
  if interrupt:
    running = False
    return
  
  totalSeconds = (float(goal)-currentTimeMillis())/1000
  min = int(totalSeconds/60)
  sec = int(totalSeconds - (60 * min))

  minstr = str(min)
  if len(str(sec)) == 1:
    secstr = "0" + str(sec)
  else:
    secstr = str(sec)

  timer.configure(text=minstr + ":" + secstr)

  if (min <= 0) and (sec <= 0):
    timer.after(resetInterval, lambda: stopTimer(timer))
    running = False
  else:
    timer.after(tickInterval, lambda: tick(timer, goal))
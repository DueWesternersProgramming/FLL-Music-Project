"""Module to control the timer being displayed in the gui"""
import time
from tkinter import TclError
from .. import shared_functions as sf

MASTERMIN = 2
MASTERSEC = 30

TICKINTERVAL = 50       # ms
RESETINTERVAL = 5000    # ms

INTERRUPT = False
RUNNING = False

def update_size(t, size):
    """Function actually changes the size of the text"""
    try:
        t.configure(font=("Serif", size))
    except TclError as e:
        sf.report_error("Error in timer.py update_size()\n" + str(t) + ", " + str(size) + "\n", e)

def current_time_millis():
    """Function returns the current time in ms"""
    return float(round(time.time()*1000))

def start_timer(timer):
    """Function that calculates the run time and starts the timer loop"""
    try:
        global RUNNING, INTERRUPT
        if RUNNING:
            stop_timer(timer)
            timer.after(TICKINTERVAL, lambda: start_timer(timer))
            return
        INTERRUPT = False
        RUNNING = True
        timer.configure(text=str(MASTERMIN) + ":" + str(MASTERSEC))
        milli_goal = ((MASTERMIN*60+MASTERSEC)*1000)+current_time_millis()+1000
        timer.after(TICKINTERVAL, lambda: tick(timer, milli_goal))
    except TclError as e:
        sf.report_error("Error in timer.py start_timer()\n" + timer, e)

def stop_timer(timer):
    """Function to stop/interrupt the timer loop"""
    try:
        global INTERRUPT
        INTERRUPT = True
        timer.configure(text=str(MASTERMIN) + ":" + str(MASTERSEC))
    except TclError as e:
        sf.report_error("Error in timer.py stop_timer()\n" + timer, e)

def tick(timer, goal):
    """Function loop that runs every tick to update the timer"""
    try:
        global RUNNING
        if INTERRUPT:
            RUNNING = False
            return

        total_seconds = (float(goal)-current_time_millis())/1000
        minutes = int(total_seconds/60)
        seconds = int(total_seconds - (60 * minutes))

        minstr = str(minutes)
        if len(str(seconds)) == 1:
            secstr = "0" + str(seconds)
        else:
            secstr = str(seconds)

        timer.configure(text=minstr + ":" + secstr)

        if (minutes <= 0) and (seconds <= 0):
            timer.after(RESETINTERVAL, lambda: stop_timer(timer))
            RUNNING = False
        else:
            timer.after(TICKINTERVAL, lambda: tick(timer, goal))
    except TclError as e:
        sf.report_error("Error in timer.py tick()\n"
                        + str(timer) + ", " + str(goal), e)

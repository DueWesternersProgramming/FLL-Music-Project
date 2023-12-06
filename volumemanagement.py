from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from pynput.keyboard import Key, Listener
import time

increment = 0.02
lowVolume = 0.2
highVolume = 0.5
application = "Spotify.exe"

sessions = AudioUtilities.GetAllSessions()
for session in sessions:
    volume = session._ctl.QueryInterface(ISimpleAudioVolume)

def on_press(key):
    if session.Process and session.Process.name() == application:
        previousVolume = volume.GetMasterVolume()
        if (key == (Key.page_up)):
            while previousVolume < highVolume:
                previousVolume = previousVolume + increment
                volume.SetMasterVolume(previousVolume, None)
                time.sleep(0.1)
            #time.sleep(2)
        if (key == (Key.page_down)):
            while previousVolume > lowVolume:
                previousVolume = previousVolume - increment
                volume.SetMasterVolume(previousVolume, None)
                time.sleep(0.1)
            #time.sleep(2)

with Listener(
        on_press=on_press) as listener:
    listener.join()
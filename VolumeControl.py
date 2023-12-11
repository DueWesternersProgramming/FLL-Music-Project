from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import time

increment = 0.02
lowVolume = 0.5
highVolume = 1.0
application = "Spotify.exe"

sessions = AudioUtilities.GetAllSessions()
correctSession = sessions[0]

for session in sessions:
    if session.Process and session.Process.name() == application:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        correctSession = session
        break

def volumeControl(control):
        previousVolume = volume.GetMasterVolume()
        if (control == True):
            print("volume up")
            while previousVolume < highVolume:
                if (previousVolume + increment) > highVolume:
                    previousVolume = highVolume
                else:
                    previousVolume = previousVolume + increment
                volume.SetMasterVolume(previousVolume, None)
                time.sleep(0.1)
        if (control == False):
            print("Volume down")
            while previousVolume > lowVolume:
                if (previousVolume - increment) < lowVolume:
                    previousVolume = lowVolume
                else:
                    previousVolume = previousVolume - increment
                volume.SetMasterVolume(previousVolume, None)
                time.sleep(0.1)
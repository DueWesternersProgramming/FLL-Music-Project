from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

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

def volumeControl(control, window):
        previousVolume = volume.GetMasterVolume()
        if (control == True):
            print("volume up")
            if previousVolume < highVolume:
                if (previousVolume + increment) > highVolume:
                    previousVolume = highVolume
                else:
                    previousVolume = previousVolume + increment
                volume.SetMasterVolume(previousVolume, None)
                window.after(100, lambda: volumeControl(control, window))
        if (control == False):
            print("Volume down")
            if previousVolume > lowVolume:
                if (previousVolume - increment) < lowVolume:
                    previousVolume = lowVolume
                else:
                    previousVolume = previousVolume - increment
                volume.SetMasterVolume(previousVolume, None)
                window.after(100, lambda: volumeControl(control, window))
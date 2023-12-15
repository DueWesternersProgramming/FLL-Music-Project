import platform
system = platform.system()
if system == 'Windows':
    from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
elif system == 'Linux':
    from alsaaudio import Mixer

increment = 0.02              # Increment Per Update Tick
updateTick = 100              # Update Tick Time In ms
lowVolume = 0.5               # Minimum Goal Volume For Specific Application
highVolume = 0.7              # Maximum Goal Volume For Specific Application
application = "Spotify.exe"   # Specific Application To Control (Windows)

global volume

def setVolumeControl(newLowVolume=lowVolume, newHighVolume=highVolume, newIncrement=increment):
    global lowVolume,highVolume,increment
    lowVolume = newLowVolume
    highVolume = newHighVolume
    increment = newIncrement

def initWindowsAudio():
    global volume
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name() == application:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            break

def initLinuxAudio():
    global volume
    volume = Mixer()

if system == 'Windows':
    initWindowsAudio()
elif system == 'Linux':
    initLinuxAudio()    

def runWindowUpdate(control, window, system):
    window.after(updateTick, lambda: volumeControl(control, window, system))

def getNewVolume(control, previousVolume, modifiedLow, modifiedHigh, modifiedIncrement):
    if (control == True):
        print("volume up")
        if (previousVolume + modifiedIncrement) > modifiedHigh:
            previousVolume = modifiedHigh
        else:
            previousVolume = previousVolume + modifiedIncrement
    else:
        print("Volume down")
        if (previousVolume - modifiedIncrement) < modifiedLow:
            previousVolume = modifiedLow
        else:
            previousVolume = previousVolume - modifiedIncrement
    return int(previousVolume)

def volumeControl(control, window, system):
    if (system == 'Windows'):
        previousVolume = volume.GetMasterVolume()
        if (control == True):
            if previousVolume < highVolume:
                volume.SetMasterVolume(getNewVolume(control, previousVolume, lowVolume, highVolume, increment), None)
                runWindowUpdate(control, window, system)
        if (control == False):
            if previousVolume > lowVolume:
                volume.SetMasterVolume(getNewVolume(control, previousVolume, lowVolume, highVolume, increment), None)
                runWindowUpdate(control, window, system)
    elif (system == 'Linux'):
        previousVolume = int(volume.getvolume()[0])
        if (control == True):
            if previousVolume < (highVolume*100):
                volume.setvolume(getNewVolume(control, previousVolume, (lowVolume*100), (highVolume*100), (increment*100)))
                runWindowUpdate(control, window, system)
        if (control == False):
            if previousVolume > (lowVolume*100):
                volume.setvolume(getNewVolume(control, previousVolume, (lowVolume*100), (highVolume*100), (increment*100)))
                runWindowUpdate(control, window, system)
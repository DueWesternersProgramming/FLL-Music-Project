"""Module to give volume control for the application"""
import platform
system = platform.system()
if system == 'Windows':
    from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
elif system == 'Linux':
    from alsaaudio import Mixer

INCREMENT = 0.02              # Increment Per Update Tick
UPDATETICK = 100              # Update Tick Time In ms
LOWVOLUME = 0.5               # Default Minimum Goal Volume For Specific Application
HIGHVOLUME = 0.7              # Dfault Maximum Goal Volume For Specific Application
APPLICATION = "Spotify.exe"   # Specific Application To Control (Windows)

VOLUME = None

def get_volume_application():
    """Function returns the current application for Windows audio control"""
    return APPLICATION

def set_volume_application(app):
    """Function sets the current application for Windows audio control"""
    global APPLICATION
    APPLICATION = app
    init_windows_audio()

def get_volume_control():
    """Function to return the current values of the volumes [low, high]"""
    return [LOWVOLUME*100, HIGHVOLUME*100]

def set_volume_control(new_low_volume, new_high_volume):
    """Function to set new volumes based on the inputs from the GUI"""
    global LOWVOLUME, HIGHVOLUME
    if new_low_volume < new_high_volume:
        LOWVOLUME = new_low_volume/100
        HIGHVOLUME = new_high_volume/100
        #print(LOWVOLUME,HIGHVOLUME)

def init_windows_audio():
    """Function to initialize the Windows audio engine"""
    global VOLUME
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name() == APPLICATION:
            VOLUME = session._ctl.QueryInterface(ISimpleAudioVolume)
            break

def init_linux_audio():
    """Function to initialize the Linux audio engine"""
    global VOLUME
    VOLUME = Mixer()

if system == 'Windows':
    init_windows_audio()
elif system == 'Linux':
    init_linux_audio()

def run_window_update(control, window, os):
    """Function to return to the main thread until the next UPDATETICK time"""
    window.after(UPDATETICK, lambda: volume_control(control, window, os))

def get_new_volume(control, previous_volume, modified_low, modified_high, modified_increment):
    """Function to return the new volume for the volume_control function"""
    if control is True:
        #print("volume up")
        if (previous_volume + modified_increment) > modified_high:
            previous_volume = modified_high
        else:
            previous_volume = previous_volume + modified_increment
    else:
        #print("Volume down")
        if (previous_volume - modified_increment) < modified_low:
            previous_volume = modified_low
        else:
            previous_volume = previous_volume - modified_increment
    return previous_volume

def volume_control(control, window, os):
    """Function to run the audio volume up or down based on the os audio system"""
    if os == 'Windows':
        previous_volume = round(VOLUME.GetMasterVolume(), 2)
        if control is True:
            if previous_volume < HIGHVOLUME:
                VOLUME.SetMasterVolume(round(get_new_volume(control, previous_volume, LOWVOLUME,
                                                      HIGHVOLUME, INCREMENT), 2), None)
                run_window_update(control, window, os)
        elif control is False:
            if previous_volume > LOWVOLUME:
                VOLUME.SetMasterVolume(round(get_new_volume(control, previous_volume, LOWVOLUME,
                                                      HIGHVOLUME, INCREMENT), 2), None)
                run_window_update(control, window, os)
    elif os == 'Linux':
        previous_volume = int(VOLUME.getvolume()[0])
        if control is True:
            if previous_volume < (HIGHVOLUME*100):
                VOLUME.setvolume(int(get_new_volume(control, previous_volume, (LOWVOLUME*100),
                                                (HIGHVOLUME*100), (INCREMENT*100))))
                run_window_update(control, window, os)
        elif control is False:
            if previous_volume > (LOWVOLUME*100):
                VOLUME.setvolume(int(get_new_volume(control, previous_volume, (LOWVOLUME*100),
                                                (HIGHVOLUME*100), (INCREMENT*100))))
                run_window_update(control, window, os)

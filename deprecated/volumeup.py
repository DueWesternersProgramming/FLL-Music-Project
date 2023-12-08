from pynput.keyboard import Key,Controller,Listener
keyboard = Controller()
import time

def on_press(key):
    if (key == (Key.page_up)):
        for i in range(10):
            keyboard.press(Key.media_volume_up)
            keyboard.release(Key.media_volume_up)
            time.sleep(0.1)
        time.sleep(2)
    if (key == (Key.page_down)):
        for i in range(8):
            keyboard.press(Key.media_volume_down)
            keyboard.release(Key.media_volume_down)
            time.sleep(0.1)
        time.sleep(2)

with Listener(
        on_press=on_press) as listener:
    listener.join()
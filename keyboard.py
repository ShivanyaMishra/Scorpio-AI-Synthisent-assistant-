from pynput.keyboard import Key, Controller # type: ignore
import screen_brightness_control as sbc # type: ignore
from time import sleep

keyboard = Controller()

def Volume_Up():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)
def Volume_Down():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)

def brightness_up():
    current_brightness = sbc.get_brightness(display=0)[0]  # Assuming display 0
    sbc.set_brightness(min(current_brightness + 10, 100))

def brightness_down():
    current_brightness = sbc.get_brightness(display=0)[0]
    sbc.set_brightness(max(current_brightness - 10, 0))

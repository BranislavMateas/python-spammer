from pynput.keyboard import Key, Controller
import time

time.sleep(5)

keyboard = Controller()

nick = "@Železo"

for i in range(10):
    keyboard.type(nick)
    time.sleep(0.1)
    keyboard.press(Key.enter)
    time.sleep(0.1)
    keyboard.press(Key.enter)
    time.sleep(2)

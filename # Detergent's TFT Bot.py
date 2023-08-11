# Detergent's TFT Bot
# Branch: main

import pyautogui as auto
from python_imagesearch.imagesearch import imagesearch as search
import time

auto.FAILSAFE = False

global gamecount
gamecount = 0

# Start utility methods
def onscreen(path, precision=0.8):
    return search(path, precision)[0] != -1

def search_to(path):
    pos = search(path)
    if onscreen(path):
        auto.moveTo(pos)
        return pos

def click_key(key, delay=.1):
    auto.keyDown(key)
    time.sleep(delay)
    auto.keyUp(key)

def click_left(delay=.1):
    auto.mouseDown()
    time.sleep(delay)
    auto.mouseUp()

def click_right(delay=.1):
    auto.mouseDown(button='right')
    time.sleep(delay)
    auto.mouseUp(button='right')

def click_to(path, delay=.1):
    if onscreen(path):
        auto.moveTo(search(path))
        click_left(delay)
# End utility methods

# ... (rest of the code remains unchanged)

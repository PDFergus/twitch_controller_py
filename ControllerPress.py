from pynput.mouse import Controller
from pynput.keyboard import Key, Controller
import time


def controller_key(new_word, runtime):
    keyboard = Controller()
    key = new_word
    key_bank = ['a','w', 's', 'd','1', '2', '3', '4']
    try:
        if key in key_bank:
            key_start = 0.0
            sleeptime = 0.030
            key_end = (runtime/ sleeptime)
            while key_start < key_end:
                time.sleep(sleeptime)
                keyboard.press(key)
                #time.sleep(0.025)
                key_start +=1
            #return
            #countdown(5)
            keyboard.release(key)
        else:
            return
    except:
        pass
import multiprocessing as mp
import os
from ctypes import *
import socket
import sys
import subprocess
import time
import random
#import keyboard
import gc
from parser import parse
import threading
from pynput.mouse import Controller
from pynput.keyboard import Key, Controller
from runtime import get_runtime
from ControllerPress import controller_key


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

def controller_s(new_word, runtime):
    keyboard = Controller()
    key = new_word
    try:
        if key == 's':
            key_start = 0.0
            sleeptime = 0.030
            key_end = (runtime/ sleeptime)
            while key_start < key_end:
                time.sleep(sleeptime)
                keyboard.press(key)
                #time.sleep(0.025)
                key_start +=1
            return
            countdown(5)
            keyboard.release(key)
        else:
            pass
    except:
        pass



class wasd_controler():
    def twitch_reader():

            print('SKey')
            server = 'irc.chat.twitch.tv'
            port = 6667
            nickname = 'WhoopsItsChatBot'
            token = '******************'
            channel = '#whoopsitspete'
            sock = socket.socket()
            sock.connect((server, port))  # connect to irc server
            sock.send(f'PASS {token}\n'.encode('utf-8'))  # send oauth token
            sock.send(f'NICK {nickname}\n'.encode('utf-8'))  # send nickname of bot
            sock.send(f'JOIN {channel}\n'.encode('utf-8'))  # send join command to channel
            try:
                while True:
                    info = list(parse(sock))
                    new_word = info[0]
                    runtime = info[1]

                    controller_s(new_word,runtime)


            except:
                wasd_controler.twitch_reader()



if __name__ == '__main__':
    jobs = []
    reader = wasd_controler.twitch_reader()
    p = mp.Process (target = reader)
    jobs.append(p)
    p.start




import multiprocessing as mp
import os
from ctypes import *
import socket
import sys
import subprocess
import time
import random
import keyboard
import gc
import threading
from pynput.mouse import Controller
from pynput.keyboard import Key, Controller
def controller_space(new_word):
    keyboard = Controller()
    key = new_word
    try:
        if key == 'jump':
            keyboard.press(Key.space)
            keyboard.release(key)
        else:
            pass
    except:
        pass



class wasd_controler():
    def twitch_reader():
        try:
            print('SpaceBar')
            server = 'irc.chat.twitch.tv'
            port = 6667
            nickname = 'WhoopsItsChatBot'
            token = 'oauth:9d71gzvktcnk84qx8ov7i2uubdvrr8'
            channel = '#whoopsitspete'
            sock = socket.socket()
            sock.connect((server, port))  # connect to irc server
            sock.send(f'PASS {token}\n'.encode('utf-8'))  # send oauth token
            sock.send(f'NICK {nickname}\n'.encode('utf-8'))  # send nickname of bot
            sock.send(f'JOIN {channel}\n'.encode('utf-8'))  # send join command to channel
            while True:
                path = ''
                resp = sock.recv(2048).decode('utf-8')  # recieve response
                if resp.startswith('PING'):  # check if response has PING and send PONG to ensure the connection stays open
                    sock.send('PONG\n'.encode('utf-8'))
                lst = resp.strip()  # create striped response
                new_lst = (lst.split())  # parse striped response into individual words
                if resp != '':  # if the response is not empty
                    for word in new_lst:  # itterate through words of the resp
                        new_word = word.lstrip(':')
                        new_word = new_word.lower()
                        try:
                            controller_space(new_word)
                            continue
                        except Exception as e:
                            pass
                        continue
        except:
            wasd_controler.twitch_reader()



if __name__ == '__main__':
    jobs = []
    reader = wasd_controler.twitch_reader()
    p = mp.Process (target = reader)
    jobs.append(p)
    p.start




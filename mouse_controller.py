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
import threading
from pynput.mouse import Button,Controller
from pynput.keyboard import Key, Controller


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
def get_runtime(raw_time):
    runtime =raw_time/0.030
    if runtime <= 334:
        return raw_time
    else:
        pass
def controller_mouse1(new_word, runtime):
    mouse = Controller()
    key = new_word
    try:
        if key == 'shoot':
            key_start = 0.0
            sleeptime = 0.030
            key_end = (runtime/ sleeptime)
            while key_start < key_end:
                time.sleep(sleeptime)
                mouse.press(Button.left)
                #time.sleep(0.025)
                key_start +=1
            #return
            #countdown(5)
            mouse.release(Button.left)
        else:
            pass
    except:
        pass



class wasd_controler():
    def twitch_reader():
        print('M1Controller')
        server = 'irc.chat.twitch.tv'
        port = 6667
        nickname = 'WhoopsItsChatBot'
        token = 'oauth:*****************'
        channel = '#whoopsitspete'
        sock = socket.socket()
        sock.connect((server, port))  # connect to irc server
        sock.send(f'PASS {token}\n'.encode('utf-8'))  # send oauth token
        sock.send(f'NICK {nickname}\n'.encode('utf-8'))  # send nickname of bot
        sock.send(f'JOIN {channel}\n'.encode('utf-8'))  # send join command to channel
        while True:
            # print('made it to res')
            path = ''
            resp = sock.recv(2048).decode('utf-8')  # recieve response
            if resp.startswith('PING'):  # check if response has PING and send PONG to ensure the connection stays open
                sock.send('PONG\n'.encode('utf-8'))
            # print(resp)
            lst = resp.strip()  # create striped response
            new_lst = (lst.split())  # parse striped response into individual words
            if resp != '':  # if the response is not empy
                #print('reading: ' + resp)
                for word in new_lst:  # itterate through words of the resp

                    new_word = word.lstrip(':')
                    new_word = new_word.lower()
                    try:
                        raw_time = int(new_word)
                        runtime = get_runtime(raw_time)
                    except Exception as e:
                        pass
                    try:
                        controller_mouse1(new_word, runtime)
                        continue
                    except Exception as e:
                        pass
                    continue
        print(f'Hi, {name}')



if __name__ == '__main__':
    jobs = []
    reader = wasd_controler.twitch_reader()
    p = mp.Process (target = reader)
    jobs.append(p)
    p.start




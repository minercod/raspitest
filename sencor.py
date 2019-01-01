#!/usr/bin/python3
#coding=utf-8

import RPi.GPIO as GP
import time

def detect():
    channel = 8
    GP.setmode(GP.BOARD)
    GP.setup(channel, GP.IN)

    while True:
        curtime = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        if GP.input(channel)==1:
            print(curtime + '......Detect someone!')
        time.sleep(1)


if __name__ == '__main__':
    try:
        detect()
    except:
        GP.cleanup()


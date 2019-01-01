#!/usr/bin/python3
#coding=utf-8

import RPi.GPIO as GP
import time

def ranging():
    trig_channel = 8
    echo_channel = 10
    GP.setmode(GP.BOARD)
    GP.setup(trig_channel, GP.OUT, initial = GP.LOW)
    GP.setup(echo_channel, GP.IN)

    time.sleep(2)
    
    GP.output(trig_channel, GP.HIGH)
    time.sleep(0.00015)
    GP.output(trig_channel, GP.LOW)
    while not GP.input(echo_channel):
        pass
    t1 = time.time()
    while GP.input(echo_channel):
        pass
    t2 = time.time()
    return (t2-t1)*340/2

if __name__ == '__main__':
    try:
        while True:
            print('Distance is %0.3f m'%ranging())
            time.sleep(1)
    except:
        GP.cleanup()



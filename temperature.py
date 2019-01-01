#!/usr/bin/python3
#coding=utf-8

import RPi.GPIO as gpio
import time

def driver():
    data = [0 for i in range(40)]
    j = 0
    channel = 15
    gpio.setmode(gpio.BOARD)
    time.sleep(1)

    gpio.setup(channel, gpio.OUT)
    gpio.output(channel, gpio.LOW)

    time.sleep(0.02)

    gpio.output(channel, gpio.HIGH)
    gpio.setup(channel, gpio.IN)

    while gpio.input(channel) == gpio.LOW:
        continue
    while gpio.input(channel) == gpio.HIGH:
        continue
    while j < 40:
        k = 0
        while gpio.input(channel) == gpio.LOW:
            continue
        while gpio.input(channel) == gpio.HIGH:
            k += 1
            if k > 100:
                break
        if k < 8:
            data[j] = 0
        else:
            data[j] = 1
        j += 1
    return data

def compute(data):
    humidity_bit = data[0:8]
    humidity_point_bit = data[8:16]
    temperature_bit = data[16:24]
    temperature_point_bit = data[24:32]
    check_bit = data[32:40]
    humidity = int(''.join([str(x) for x in humidity_bit]), 2)
    humidity_point = int(''.join([str(x) for x in humidity_point_bit]), 2)
    temperature = int(''.join([str(x) for x in temperature_bit]), 2)
    temperature_point = int(''.join([str(x) for x in temperature_point_bit]), 2)
    check_num = int(''.join([str(x) for x in check_bit]), 2)
    sum = humidity + humidity_point + temperature + temperature_point 
    gpio.cleanup()
    while sum == check_num:
        print('Data is correct, temp:%d,hum:%d%%.'%(temperature, humidity))
        time.sleep(3)
        compute(driver())
    else:
        print('Warning:Data is not correct,restart recieving data...')
        time.sleep(3)
        compute(driver())

if __name__ == '__main__':
    try:
        compute(driver())
    except:
        GP.cleanup()



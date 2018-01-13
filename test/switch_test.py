#!/usr/bin/env python3

#
# Nova Labs space_switch

#import network, requests, json, time, math
import signal
import sys
import time
#from machine import Pin
import RPi.GPIO as GPIO


SWITCH_GPIO = 23

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(SWITCH_GPIO, GPIO.OUT)

print("GPIO pin %d", SWITCH_GPIO)
print("GPIO mode %d", GPIO.getmode())

def signal_handler(signal, frame):
        sys.exit(0)
    

old_switch_state = GPIO.input(SWITCH_GPIO)
print("start switch state: %d", old_switch_state)

while True:
    current_switch_state = GPIO.input(SWITCH_GPIO)
    if old_switch_state == current_switch_state:
        time.sleep(.01)
        continue
    old_switch_state = current_switch_state
    print("switch state: %d", old_switch_state)

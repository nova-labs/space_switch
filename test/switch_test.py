#!/usr/bin/env python3

#
# Nova Labs space_switch

#import network, requests, json, time, math
import signal
import sys
import time
#from machine import Pin
import RPi.GPIO as GPIO


SWITCH_ONE_GPIO = 22
SWITCH_TWO_GPIO = 27

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(SWITCH_ONE_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_TWO_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("GPIO pin %d", SWITCH_ONE_GPIO)
print("GPIO mode %d", GPIO.getmode())

def signal_handler(signal, frame):
        sys.exit(0)
    

old_switch_one_state = GPIO.input(SWITCH_ONE_GPIO)
old_switch_two_state = GPIO.input(SWITCH_TWO_GPIO)
print("start switch state: %d", old_switch_state)

while True:
    current_switch_one_state = GPIO.input(SWITCH_ONE_GPIO)
    current_switch_two_state = GPIO.input(SWITCH_TWO_GPIO)
    if old_switch_one_state == current_switch_one_state & old_switch_two_state == current_switch_two_state:
        time.sleep(.01)
        continue
    old_switch_one_state = current_switch_one_state
    old_switch_two_state = current_switch_two_state
    print("SWITCH: new values %d - %d" % (current_switch_one_state, current_switch_two_state))

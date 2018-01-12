#!/usr/bin/env python3

import time
from neopixel import *

LED_COUNT = 12
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 5
LED_INVERT = False


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
strip.begin()

print("Press Ctrl-c to quit")
while True:
    colorWipe(strip, Color(255,0,0))
    colorWipe(strip, Color(0,255,0))
    colorWipe(strip, Color(0,0,255))
    

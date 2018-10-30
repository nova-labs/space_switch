#!/usr/bin/env python3

import time
import board
import neopixel

LED_COUNT = 10

ORDER = neopixel.GRB
pixel_pin = board.D18


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(LED_COUNT):
        strip[i] = color
        strip.show()
        time.sleep(wait_ms/1000.0)


pixels = neopixel.NeoPixel(pixel_pin, LED_COUNT, brightness=0.2, auto_write=False, pixel_order=ORDER)

print("Press Ctrl-c to quit")
while True:
    colorWipe(pixels, (255, 0, 0))
    colorWipe(pixels, (0, 255, 0))
    colorWipe(pixels, (0, 0, 255))
    colorWipe(pixels, (255, 165, 0))
    colorWipe(pixels, (110, 60, 0))
    colorWipe(pixels, (90, 45, 0))
    colorWipe(pixels, (60, 40, 0))

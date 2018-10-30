#!/usr/bin/env python3

# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import argparse
import signal
import sys
import time
import board
import neopixel


def signal_handler(signal, frame):
    colorWipe(strip, (0, 0, 0))
    sys.exit(0)


def opt_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', action='store_true', help='clear the display on exit')
    args = parser.parse_args()
    if args.c:
        signal.signal(signal.SIGINT, signal_handler)


# LED strip configuration:
LED_COUNT = 10  # Number of LED pixels.
ORDER = neopixel.GRB
pixel_pin = board.D18


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(LED_COUNT):
        strip[i] = color
        strip.show()
        time.sleep(wait_ms / 1000.0)


def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, LED_COUNT, 3):
                if (i + q) < LED_COUNT:
                    strip[i + q] = color
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, LED_COUNT, 3):
                if (i + q) < LED_COUNT:
                    strip[i + q] = 0


def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)


def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256 * iterations):
        for i in range(LED_COUNT):
            strip[i] = wheel((i + j) & 255)
        strip.show()
        time.sleep(wait_ms / 1000.0)


def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256 * iterations):
        for i in range(LED_COUNT):
            strip[i] = wheel((int(i * 256 / LED_COUNT) + j) & 255)
        strip.show()
        time.sleep(wait_ms / 1000.0)


def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, LED_COUNT, 3):
                if (i + q) < LED_COUNT:
                    strip[i + q] = wheel((i + j) % 255)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, LED_COUNT, 3):
                if (i + q) < LED_COUNT:
                    strip[i + q] = 0


# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    opt_parse()

pixels = neopixel.NeoPixel(pixel_pin, LED_COUNT, brightness=0.2, auto_write=False, pixel_order=ORDER)

print ('Press Ctrl-C to quit.')
while True:
    print ('Color wipe animations.')
    colorWipe(pixels, (255, 0, 0))  # Red wipe
    colorWipe(pixels, (0, 255, 0))  # Blue wipe
    colorWipe(pixels, (0, 0, 255))  # Green wipe
    print ('Theater chase animations.')
    theaterChase(pixels, (127, 127, 127))  # White theater chase
    theaterChase(pixels, (127, 0, 0))  # Red theater chase
    theaterChase(pixels, (0, 0, 127))  # Blue theater chase
    print ('Rainbow animations.')
    rainbow(pixels)
    rainbowCycle(pixels)
    theaterChaseRainbow(pixels)

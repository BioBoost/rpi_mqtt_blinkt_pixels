#!/usr/bin/env python3

from time import sleep
import sys
from lib.pixels.blinkt_strip import *
from lib.pixels.neopixel_strip import *
from lib.mqtt_strip import *

BROKER_ADDRESS = "localhost"

LED_COUNT      = 78                 # Number of LED pixels.
LED_PIN        = 18                 # GPIO pin connected to the pixels (must support PWM!).

if __name__ == '__main__':
    strip = NeopixelStrip(LED_COUNT, LED_PIN)
    mqttStrip = MqttStrip(strip, BROKER_ADDRESS, "thumper", "neopixels")

    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:       # Catch CTRL-C
        mqttStrip.stop()
        print("Bye Bye")
        sys.exit()

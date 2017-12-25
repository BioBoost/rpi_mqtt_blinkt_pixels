#!/usr/bin/env python3

from time import sleep
import sys
from lib.pixel_strip import *
from lib.saito_bed import *

BROKER_ADDRESS = "10.0.0.100"

if __name__ == '__main__':
    strip = PixelStrip()
    bed = SaitoBed(strip, BROKER_ADDRESS)

    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:       # Catch CTRL-C
        bed.stop()
        print("Bye Bye")
        sys.exit()

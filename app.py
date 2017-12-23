from time import sleep
import sys
from lib.pixel_strip import *
from lib.color import *

if __name__ == '__main__':
    strip = PixelStrip()
    strip.set_all(Colors.ORANGE)

    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:       # Catch CTRL-C
        print ("Bye Bye")
        sys.exit()

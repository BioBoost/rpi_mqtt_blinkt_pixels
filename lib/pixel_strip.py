import blinkt
from lib.color import *

class PixelStrip(object):
    def __init__(self):
        blinkt.set_clear_on_exit()
        self.color = Colors.BLACK
        self.brightness = 255
        self.off()

    def set_all(self, color, brightness=255, retain=True):
        if retain:
            self.color = color
            self.brightness = brightness

        blinkt.set_all(color.red(), color.green(), color.blue(), brightness/255)
        blinkt.show()

    def set(self, index, color, brightness=255):
        blinkt.set_pixel(index, color.red(), color.green(), color.blue())
        blinkt.set_brightness(brightness/255)
        blinkt.show()

    def off(self):
        blinkt.clear()
        self.isOn = False

    def on(self):
        self.set_all(self.color, self.brightness)
        self.isOn = True

    def number_of_pixels(self):
        return blinkt.NUM_PIXELS

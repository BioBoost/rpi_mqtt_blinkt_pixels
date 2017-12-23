import blinkt
from lib.color import *

class PixelStrip(object):
    def __init__(self):
        blinkt.set_clear_on_exit()
        self.color = Colors.BLACK
        self.off()

    def set_all(self, color, retainColor=True):
        self.color = color if retainColor else self.color
        blinkt.set_all(color.red(), color.green(), color.blue())
        blinkt.show()

    def set(self, index, color):
        blinkt.set_pixel(index, color.red(), color.green(), color.blue())
        blinkt.show()

    def off(self):
        blinkt.clear()
        self.isOn = False

    def on(self):
        self.set_all(self.color)
        self.isOn = True

    def number_of_pixels(self):
        return blinkt.NUM_PIXELS

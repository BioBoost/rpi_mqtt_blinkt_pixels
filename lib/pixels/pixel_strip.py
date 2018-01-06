from lib.color import *

class PixelStrip(object):
    def __init__(self):
        self.color = Colors.BLACK
        self.brightness = 255

    def set_all(self, color, brightness=255, retain=True):
        if retain:
            self.color = color
            self.brightness = brightness

    def set(self, index, color, brightness=255):
        pass

    def off(self):
        self.isOn = False

    def on(self):
        self.isOn = True

    def number_of_pixels(self):
        return 0

import blinkt
from lib.pixels.pixel_strip import *

class BlinktStrip(PixelStrip):
    def __init__(self):
        super().__init__()
        blinkt.set_clear_on_exit()
        self.off()

    def set_all(self, color, brightness=255, retain=True):
        super().set_all(color, brightness, retain)
        blinkt.set_all(color.red(), color.green(), color.blue(), brightness/255)
        blinkt.show()

    def set(self, index, color, brightness=255):
        blinkt.set_pixel(index, color.red(), color.green(), color.blue())
        blinkt.set_brightness(brightness/255)
        blinkt.show()

    def off(self):
        blinkt.clear()
        super().off()

    def on(self):
        self.set_all(self.color, self.brightness)
        super().on()

    def number_of_pixels(self):
        return blinkt.NUM_PIXELS

from lib.color import *
from lib.effects.effect import *
import colorsys
import time
from lib.wheel import wheel

class RainbowEffect(Effect):

    def __init__(self, pixelStrip, brightness=255, updateInterval=0.5):
        super().__init__(pixelStrip, Colors.WHITE, brightness, updateInterval)
        self.iteration = 0

    def start(self):
        """ Implement the starting of the effect here """
        self.pixelStrip.set_all(Colors.BLACK)
        self.iteration = 0

    def stop(self):
        """ Implement the stopping of the effect here """
        self.pixelStrip.set_all(Colors.BLACK)

    def run(self):
        """ Implement the actual effect here """
        for i in range(self.pixelStrip.number_of_pixels()):
            self.pixelStrip.set(i, wheel((i+self.iteration) & 255), self.brightness)

        self.iteration += 1

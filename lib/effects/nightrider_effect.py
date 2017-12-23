from lib.color import *
from lib.effects.effect import *

class NightRiderEffect(Effect):

    def __init__(self, pixelStrip, color=Colors.WHITE, updateInterval=1.0):
        super().__init__(pixelStrip, updateInterval)
        self.color = color

    def start(self):
        """ Implement the starting of the effect here """
        self.pixelStrip.set_all(Colors.BLACK)
        self.currentLed = 0
        self.delta = 1

    def stop(self):
        """ Implement the stopping of the effect here """
        self.pixelStrip.set_all(Colors.BLACK)

    def run(self):
        """ Implement the actual effect here """
        self.pixelStrip.set_all(Colors.BLACK)
        self.pixelStrip.set(self.currentLed, self.color)
        self.currentLed = (self.currentLed + self.delta)

        if self.currentLed >= self.pixelStrip.number_of_pixels()-1 or self.currentLed <= 0:
            self.delta = -self.delta

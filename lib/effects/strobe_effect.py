from lib.color import *
from lib.effects.effect import *

class StrobeEffect(Effect):

    def __init__(self, pixelStrip, color=Colors.WHITE, brightness=255, updateInterval=1.0):
        super().__init__(pixelStrip, color, brightness, updateInterval)

    def start(self):
        """ Implement the starting of the effect here """
        self.pixelStrip.set_all(Colors.BLACK)
        self.strobe = True

    def stop(self):
        """ Implement the stopping of the effect here """
        self.pixelStrip.set_all(Colors.BLACK)

    def run(self):
        """ Implement the actual effect here """
        if self.strobe:
            self.pixelStrip.set_all(self.color, self.brightness)
        else:
            self.pixelStrip.set_all(Colors.BLACK)

        self.strobe = not self.strobe

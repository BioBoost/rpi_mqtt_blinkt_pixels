from lib.color import *
from lib.effects.effect import *

class ColorEffect(Effect):

    def __init__(self, pixelStrip, color=Colors.WHITE, brightness=255):
        super().__init__(pixelStrip, color, brightness)

    def start(self):
        """ Implement the starting of the effect here """
        pass

    def stop(self):
        """ Implement the stopping of the effect here """
        self.pixelStrip.set_all(Colors.BLACK)

    def run(self):
        """ Implement the actual effect here """
        self.pixelStrip.set_all(self.color, self.brightness)

from lib.color import *
from lib.effects.effect import *

class GroupShiftEffect(Effect):

    def __init__(self, pixelStrip, color=Colors.WHITE, brightness=255, updateInterval=1.0, groupSize=8):
        super().__init__(pixelStrip, color, brightness, updateInterval)
        self.set_group_size(groupSize)

    def start(self):
        """ Implement the starting of the effect here """
        self.pixelStrip.set_all(Colors.BLACK)
        self.currentIndex = 0

    def stop(self):
        """ Implement the stopping of the effect here """
        self.pixelStrip.set_all(Colors.BLACK)

    def run(self):
        """ Implement the actual effect here """
        self.pixelStrip.set_all(Colors.BLACK)

        for g in range(self.numberOfGroups):
            i = (g * self.groupSize) + self.currentIndex
            self.pixelStrip.set(i, self.color, self.brightness)

        self.currentIndex = (self.currentIndex + 1) % self.groupSize

    def set_group_size(self, size):
        self.groupSize = size
        self.numberOfGroups = self.pixelStrip.number_of_pixels() // self.groupSize

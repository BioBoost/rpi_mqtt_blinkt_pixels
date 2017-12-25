from lib.color import *

class Effect(object):

    def __init__(self, pixelStrip, updateInterval=1.0):
        self.pixelStrip = pixelStrip
        self.updateInterval = updateInterval
        self.color = Colors.BLACK

    def start(self):
        """ Implement the starting of the effect here """
        raise NotImplementedError("Please Implement this method")

    def stop(self):
        """ Implement the stopping of the effect here """
        raise NotImplementedError("Please Implement this method")

    def run(self):
        """ Implement the actual effect here """
        raise NotImplementedError("Please Implement this method")

    def get_color(self):
        return self.color

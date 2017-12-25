from lib.color import *

class Effect(object):

    def __init__(self, pixelStrip, color=Colors.BLACK, brightness=255, updateInterval=1.0):
        self.pixelStrip = pixelStrip
        self.updateInterval = updateInterval
        self.set_color(color)
        self.set_brightness(brightness)

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

    def get_brightness(self):
        return self.brightness

    def set_brightness(self, brightness):
        self.brightness = brightness

    def set_color(self, color):
        self.color = color

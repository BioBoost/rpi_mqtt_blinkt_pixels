from neopixel import *
from lib.pixels.pixel_strip import *

class NeopixelStrip(PixelStrip):
	# LED strip configuration:
	LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
	LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
	LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

	def __init__(self, numberOfLeds, pin):
		super().__init__()
		self.strip = Adafruit_NeoPixel(numberOfLeds, pin,	\
			NeopixelStrip.LED_FREQ_HZ, NeopixelStrip.LED_DMA, \
			NeopixelStrip.LED_INVERT, self.brightness)

		# Intialize the library (must be called once before other functions).
		self.strip.begin()
		self.off()

	def set_all(self, color, brightness=255, retain=True):
		super().set_all(color, brightness, retain)

		for i in range(0, self.strip.numPixels()):
			self.strip.setPixelColorRGB(i, color.red(), color.green(), color.blue())
		self.strip.setBrightness(brightness)
		self.strip.show()

	def set(self, index, color, brightness=255):
		self.strip.setPixelColorRGB(index, color.red(), color.green(), color.blue())
		self.strip.setBrightness(brightness)
		self.strip.show()

	def off(self):
		self.set_all(Colors.BLACK, 0, False)
		super().off()

	def on(self):
		self.set_all(self.color, self.brightness)
		super().on()

	def number_of_pixels(self):
		return self.strip.numPixels()

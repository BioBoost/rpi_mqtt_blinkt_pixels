class Color:
    def __init__(self, red, green, blue):
        self.set(red, green, blue)

    def set(self, red, green, blue):
        self.r = red
        self.g = green
        self.b = blue

    def set_hex(self, hex):
        raise NotImplementedError

    def red(self):
        return self.r

    def green(self):
        return self.g

    def blue(self):
        return self.b

class Colors(object):
    RED = Color(255, 0, 0)
    GREEN = Color(0, 255, 0)
    BLUE = Color(0, 0, 255)
    WHITE = Color(255, 255, 255)
    BLACK = Color(0, 0, 0)
    YELLOW = Color(255, 255, 0)
    MAGENTA = Color(255, 0, 255)
    CYAN = Color(0, 255, 255)
    ORANGE = Color(255, 69, 0)

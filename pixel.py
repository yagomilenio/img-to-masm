class Pixel:
    def __init__(self, color, x, y):
        self.x=x
        self.y=y
        self.color=color

class PixelGroup:
    def __init__(self, color, x, y, repeats):
        self.x=x
        self.y=y
        self.color=color
        self.repeats=repeats
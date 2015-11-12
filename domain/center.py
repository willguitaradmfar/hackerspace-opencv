import numpy as np

from box import Box

class Center(Box):
    def __init__(self, x, y, w, h, id):
        Box.__init__(self, x, y, w, h, id)
        self.px = self.x + (self.w/2)
        self.py = self.y + (self.h/2)

import numpy as np

from src.domain.point import Point

class Box:
    def __init__(self, x, y, w, h, id):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.id = id

    def setLabel(self, label):
        label.draw(Point(self.x + self.w, self.y));

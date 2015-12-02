import numpy as np
import json

from src.domain.box import Box

class Center(Box):
    def __init__(self, x, y, w, h, id):
        Box.__init__(self, x, y, w, h, id)
        self.poly = None
        self.px = self.x + (self.w/2)
        self.py = self.y + (self.h/2)
        self.poly = None
        self.maxH = 0
        self.maxA = 0

    def setPoly(self, poly):
        self.poly = poly

    def getMetrica(self):
        preoduto = self.w + self.h
        percW = (self.w*100)/preoduto
        percH = 100 - percW

        return percW,percH

    def toJSON(self):
        d = dict()
        d['x'] = self.px
        d['y'] = self.py
        return json.dumps(d)

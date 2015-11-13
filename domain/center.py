import numpy as np

from box import Box

class Center(Box):
    def __init__(self, x, y, w, h, id):
        Box.__init__(self, x, y, w, h, id)
        self.poly = None
        self.px = self.x + (self.w/2)
        self.py = self.y + (self.h/2)
        self.areaName = None
        self.maxH = 0
        self.maxA = 0

    def setAreaName(self, areaName):
        self.areaName = areaName

    def getMetrica(self):
        preoduto = self.w + self.h
        percW = (self.w*100)/preoduto
        percH = 100 - percW

        return percW,percH

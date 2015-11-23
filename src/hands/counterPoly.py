import numpy as np
import cv2

from src.util.geometria import Geometria

geometria = Geometria()

class CounterPoly:
    def __init__(self):
        self._centers = None
        self.areas = dict();

    def setCenters(self, centers):
        if self._centers == None:
            self._centers = centers
            return

        for center in centers:
            for _center in self._centers:
                if center.poly != None and _center.poly != None:
                    if _center.id == center.id and _center.poly.name != center.poly.name:
                        try:
                            self.areas[center.poly.name] += 1
                        except:
                            self.areas[center.poly.name] = 1

        self._centers = centers

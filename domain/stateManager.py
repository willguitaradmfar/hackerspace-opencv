import numpy as np
import cv2

from utils.geometria import Geometria

geometria = Geometria()

class StateManager:
    def __init__(self):
        self._centers = None
        self.areas = dict();

    def setCenters(self, centers):
        if self._centers == None:
            self._centers = centers
            return

        for center in centers:
            for _center in self._centers:
                if _center.id == center.id and _center.areaName != center.areaName:
                    try:
                        self.areas[center.areaName] += 1
                    except:
                        self.areas[center.areaName] = 1
                        
        self._centers = centers

import numpy as np
import cv2

from utils.geometria import Geometria
from utils.crop import Crop

from domain.point import Point

from domain.label import Label

g = Geometria();
c = Crop()

class Identify:
    def __init__(self, M=20):
        self._centers = None
        self.M = M
        self.color = (0,255,0)
        self.colorFont = (255,255,0)
        print("M: %s" % self.M)

    def setTrack(self, track):
        self.track = track

    def getPointsMap(self, dictPoly):
        if self._centers == None:
            self._centers = self.track.getCenters()
            return None

        centers = self.track.getCenters()

        for center in centers:
            for _center in self._centers:
                h = g.distance((_center.x, _center.y), (center.x, center.y))
                if self.M > h:
                    center.id = _center.id
                    cv2.rectangle(self.track.frame,(center.x,center.y),(center.x+center.w,center.y+center.h),self.color,1)
                    hasPoly = False
                    for poly in dictPoly:
                        if dictPoly[poly].containsPoint(Point(center.px, center.py)):
                            area = center.w * center.h
                            texts = [("ID: %0.0f" % (center.id)), ("A: %0.0f" % area),("H: %0.0f" % h), (poly)]
                            Label(self.track.frame, center, texts)
                            hasPoly = True
                    if not hasPoly:
                        area = center.w * center.h
                        texts = [("ID: %0.0f" % (center.id)), ("A: %0.0f" % area), ("H: %0.0f" % h), ("Sem area")]
                        Label(self.track.frame, center, texts)

        self._centers = centers

        return centers

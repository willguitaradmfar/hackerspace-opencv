import numpy as np
import cv2

from utils.geometria import Geometria
from utils.crop import Crop

from domain.point import Point

from domain.label import Label

g = Geometria();

# OBJETO RESPONSÁVEL POR IDENTIFICAR OBJETOS UNICOS NO PLANO
# RECEBE UMA INSTANCIA DO OBJETO Moviment

class Identify:
    def __init__(self, M=20):
        self._centers = None
        self.M = M
        self.color = (0,255,0)
        self.colorFont = (255,255,0)
        print("M: %s" % self.M)

    def setMoviment(self, moviment):
        self.moviment = moviment


    # RETORNA UM ARRAY DE CENTROIDES IDENTIFICADOS COM ID E COM A ÁREA QUE PERTENCE
    # A ÁREA É PASSADO EM FORMA DE DICIONÁRIO DE OBJETOS [Polygon]
    def getPointsMap(self, dictPoly):
        if self._centers == None:
            self._centers = self.moviment.getCenters()
            return None

        # RECUPERA TODOS OS CENTRÓIDES
        centers = self.moviment.getCenters()

        for center in centers:
            for _center in self._centers:
                h = g.distance((_center.x, _center.y), (center.x, center.y))
                if self.M > h:
                    center.id = _center.id
                    center.maxH = _center.maxH
                    center.maxA = _center.maxA
                    cv2.rectangle(self.moviment.frame,(center.x,center.y),(center.x+center.w,center.y+center.h),self.color,1)
                    hasPoly = False
                    for poly in dictPoly:
                        if dictPoly[poly].containsPoint(Point(center.px, center.py)):
                            area = center.w * center.h
                            if center.maxH < h:
                                center.maxH = h
                            if center.maxA < area:
                                center.maxA = area

                            texts = [("ID: %0.0f" % (center.id)), ("A: %0.0f" % area), ("MA: %0.0f" % center.maxA), ("H: %0.0f" % h), ("MH: %0.0f" % center.maxH), (poly)]
                            Label(self.moviment.frame, center, texts)
                            hasPoly = True
                            center.setAreaName(poly)
                    if not hasPoly:
                        area = center.w * center.h
                        texts = [("ID: %0.0f" % (center.id)), ("A: %0.0f" % area), ("H: %0.0f" % h), ("Sem area")]
                        Label(self.moviment.frame, center, texts)
                        center.setAreaName(None)

        self._centers = centers

        return centers

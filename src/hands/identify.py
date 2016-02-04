import numpy as np
import cv2

from src.util.geometria import Geometria

from src.domain.point import Point

from src.domain.label import Label

from src.domain.polygon import Polygon

g = Geometria();

polyDefault = Polygon()
polyDefault.setName("Default")

# OBJETO RESPONSAVEL POR IDENTIFICAR OBJETOS UNICOS NO PLANO
# RECEBE UMA INSTANCIA DO OBJETO Moviment

class Identify:
    def __init__(self, deslocamentoMax=20):
        self._centers = None
        Identify.deslocamentoMax = deslocamentoMax
        self.color = (0,255,0)
        self.colorFont = (255,255,0)

    def setMoviment(self, moviment):
        self.moviment = moviment


    # RETORNA UM ARRAY DE CENTROIDES IDENTIFICADOS COM ID E COM A AREA QUE PERTENCE
    # A AREA E PASSADO EM FORMA DE DICIONARIO DE OBJETOS [Polygon]
    def getPointsMap(self, arrayPoly):
        print(arrayPoly)
        if self._centers == None:
            self._centers = self.moviment.getCenters()
            return None

        if arrayPoly == None:
            arrayPoly = [];
            arrayPoly.insert(0, polyDefault)

        # RECUPERA TODOS OS CENTROIDES
        centers = self.moviment.getCenters()

        for center in centers:
            for _center in self._centers:
                h = g.distance((_center.x, _center.y), (center.x, center.y))
                if Identify.deslocamentoMax > h:
                    center.id = _center.id
                    center.maxH = _center.maxH
                    center.maxA = _center.maxA
                    
                    hasPoly = False
                    for poly in arrayPoly:
                        if poly.containsPoint(Point(center.px, center.py)):
                            hasPoly = True
                            if poly.clas == "off":
                                pass
                            else:
                                area = center.w * center.h
                                if center.maxH < h:
                                    center.maxH = h
                                if center.maxA < area:
                                    center.maxA = area

                                texts = [("ID: %0.0f" % (center.id)), (poly.name)]
                                label = Label(texts)
                                label.setFrame(self.moviment.frame)
                                center.setLabel(label)
                                center.setPoly(poly)
                                cv2.rectangle(self.moviment.frame,(center.x,center.y),(center.x+center.w,center.y+center.h),self.color,1)
                                cv2.rectangle(self.moviment.frame,(center.x+1,center.y+1),(center.x+center.w+1,center.y+center.h+1),(255,255,255),1)

                    if not hasPoly:
                        area = center.w * center.h
                        texts = [("ID: %0.0f" % (center.id)), ("A: %0.0f" % area), ("H: %0.0f" % h), ("Sem area")]
                        label = Label(texts)
                        label.setFrame(self.moviment.frame)
                        center.setLabel(label)
                        center.setPoly(polyDefault)
                        cv2.rectangle(self.moviment.frame,(center.x,center.y),(center.x+center.w,center.y+center.h),self.color,1)
                        cv2.rectangle(self.moviment.frame,(center.x+1,center.y+1),(center.x+center.w+1,center.y+center.h+1),(255,255,255),1)


        self._centers = centers

        return centers

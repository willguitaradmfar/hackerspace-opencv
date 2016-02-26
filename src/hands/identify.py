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
        Identify.mediumLine = 30000
        Identify.largeLine = 50000
        self.color = (0,255,0)
        self.colorFont = (255,255,0)
        self.areaList = []
        self.hasLine = False

    def setMoviment(self, moviment):
        self.moviment = moviment

    def lineController(self):
        pass

    # RETORNA UM ARRAY DE CENTROIDES IDENTIFICADOS COM ID E COM A AREA QUE PERTENCE
    # A AREA E PASSADO EM FORMA DE DICIONARIO DE OBJETOS [Polygon]
    def getPointsMap(self, arrayPoly, frame):
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
                #calculo a distancia entre os centros do objeto
                h = g.distance((_center.x, _center.y), (center.x, center.y))
                if Identify.deslocamentoMax > h:
                    center.id = _center.id
                    center.maxH = _center.maxH
                    center.maxA = _center.maxA
                    
                    hasPoly = False
                    for poly in arrayPoly:
                        #verifico se o centro localizado esta dentro da area
                        if poly.containsPoint(Point(center.px, center.py)):
                            hasPoly = True
                            #se o poligono for da classe off nao desenho o retangulo
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
                                #Desenho dois retangulos para destacar melhor na imagem
                                cv2.rectangle(self.moviment.frame,(center.x,center.y),(center.x+center.w,center.y+center.h),self.color,1)
                                cv2.rectangle(self.moviment.frame,(center.x+1,center.y+1),(center.x+center.w+1,center.y+center.h+1),(255,255,255),1)
                                if poly.clas == "line":
                                    #Se detectar algum movimento dentro da area, starta os processos de calculo
                                    self.hasLine = True
                                    #Aplico mascara para destacar apenas a area da fila
                                    mask = np.zeros(self.moviment.dilation.shape, dtype=np.uint8)
                                    #********Pegar os pontos do poligono de fila
                                    roi_corners = np.array([[(140,410), (340,400), (750,680), (200,680)]], dtype=np.int32)
                                    channel_count = self.moviment.dilation.shape[0]
                                    ignore_mask_color = (255,0,0)
                                    cv2.fillPoly(mask, roi_corners, ignore_mask_color)
                                    masked_image = cv2.bitwise_and(self.moviment.dilation, mask)
                                    (contours, a, _) = cv2.findContours(masked_image, 1, 2)
                                    M = cv2.moments(contours)
                                    self.area = M['m00']
                                    
                    if not hasPoly:
                        area = center.w * center.h
                        texts = [("ID: %0.0f" % (center.id)), ("A: %0.0f" % area), ("H: %0.0f" % h), ("Sem area")]
                        label = Label(texts)
                        label.setFrame(self.moviment.frame)
                        center.setLabel(label)
                        center.setPoly(polyDefault)
                        cv2.rectangle(self.moviment.frame,(center.x,center.y),(center.x+center.w,center.y+center.h),self.color,1)
                        cv2.rectangle(self.moviment.frame,(center.x+1,center.y+1),(center.x+center.w+1,center.y+center.h+1),(255,255,255),1)

        #Controle de fila por area
        if self.hasLine:
            #retorno se a fila esta cheia
            #***********Criar calculo de media
            print(self.area)
            if self.area > Identify.largeLine:
                print("Fila cheia")
            elif self.area < Identify.largeLine and self.area > Identify.mediumLine:
                print("Fila media")
            elif self.area < Identify.mediumLine:
                print("Fila pequena")
            


        self._centers = centers

        return centers

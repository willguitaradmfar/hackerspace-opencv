import numpy as np
import cv2

from src.util.geometria import Geometria

from src.domain.point import Point

geometria = Geometria()

class Polygon:
    def __init__(self, color=(255,0,0)):
        self.lines = []
        self.color = color
        self.name = "Sem nome"
        #classe do poligono, pode ser count=contagem de pessoas, line=deteccao de filas, off=nao considerar movimento 
        self.clas = "" 

    def setLabel(self, label):
        label.setColor(self.color)
        label.draw(Point(self.lines[0].pointF.x + 10, self.lines[0].pointF.y + 10));

    def setFrame(self, frame):
        self.frame = frame

    def setName(self, name):
        self.name = name

    def addLine(self, line):
        self.lines.insert(0, line)

    def containsPoint(self, point):
        return geometria.isPointInPolyAsClass(self, point)

    def draw(self):
        for line in self.lines:
            if self.clas == "off":
                self.color = color=(0,0,255)
            if self.clas == "line":
                self.color = color=(255,0,0)
            if self.clas == "count":
                self.color = color=(0,255,0)
            cv2.line(self.frame,(line.pointI.x, line.pointI.y),(line.pointF.x, line.pointF.y),self.color,3)

    def setClass(self,clas):
        self.clas = clas

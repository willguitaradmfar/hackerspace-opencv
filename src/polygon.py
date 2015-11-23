import numpy as np
import cv2

from src.geometria import Geometria

from src.point import Point

geometria = Geometria()

class Polygon:
    def __init__(self, color=(255,0,0)):
        self.lines = []
        self.color = color
        self.name = "Sem nome"

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
            cv2.line(self.frame,(line.pointI.x, line.pointI.y),(line.pointF.x, line.pointF.y),self.color,3)

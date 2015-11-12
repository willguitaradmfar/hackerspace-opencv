import numpy as np
import cv2

from utils.geometria import Geometria

geometria = Geometria()

class Polygon:
    def __init__(self, color=(255,0,0)):
        self.lines = []
        self.color = color

    def setFrame(self, frame):
        self.frame = frame

    def addLine(self, line):
        self.lines.insert(0, line)

    def conteinsPoint(self, point):
        return geometria.isPointInPolyAsClass(self, point)

    def draw(self):
        for line in self.lines:
            cv2.line(self.frame,(line.pointI.x, line.pointI.y),(line.pointF.x, line.pointF.y),self.color,3)

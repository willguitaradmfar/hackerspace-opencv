import numpy as np
import cv2

class Label:
    def __init__(self, texts):
        self.colorFont = (0,0,0)
        self.colorFontBack = (255,255,255)
        self.texts = texts;

    def setColor(self, color):
        self.colorFont = color

    def setFrame(self, frame):
        self.frame = frame

    def draw(self, point):
        for i in range(0, len(self.texts)):
            text = self.texts[i]
            cv2.putText(self.frame, text, (point.x+3, point.y+11+(i*15)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, self.colorFontBack, 1)
            cv2.putText(self.frame, text, (point.x+2, point.y+10+(i*15)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, self.colorFont, 1)

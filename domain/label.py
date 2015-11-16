import numpy as np
import cv2

class Label:
    def __init__(self, texts):
        self.colorFont = (255,255,0)
        self.texts = texts;

    def setColor(self, color):
        self.colorFont = color        

    def setFrame(self, frame):
        self.frame = frame

    def draw(self, point):
        for i in range(0, len(self.texts)):
            text = self.texts[i]
            cv2.putText(self.frame, text, (point.x+2, point.y+10+(i*15)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, self.colorFont, 1)

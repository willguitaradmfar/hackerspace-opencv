import numpy as np
import cv2

class Stream:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def getFrame(self):
        ret, frame = self.cap.read()
        return frame

    def finish(self):
        self.cap.release()

import numpy as np
import cv2

from src.stream.stream import Stream

class Cam(Stream):
    def __init__(self):
        Stream.__init__(self)
        self.cap = cv2.VideoCapture(0)

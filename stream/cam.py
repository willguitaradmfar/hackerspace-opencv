import numpy as np
import cv2

from stream import Stream

class Cam(Stream):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

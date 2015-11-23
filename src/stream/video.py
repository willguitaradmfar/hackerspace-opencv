import numpy as np
import cv2

from src.stream.stream import Stream

class Video(Stream):
    def __init__(self, path="videos/video.mp4"):
        Stream.__init__(self)
        self.cap = cv2.VideoCapture(path)

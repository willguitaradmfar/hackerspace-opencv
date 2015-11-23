import numpy as np
import cv2

from src.stream import Stream

class Video(Stream):
    def __init__(self, path="videos/video.mp4"):
        self.cap = cv2.VideoCapture(path)

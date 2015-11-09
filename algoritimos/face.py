import numpy as np
import cv2

class Face:
    def __init__(self):
        self.size = 2
        self.face_resize = None
        (self.im_width, self.im_height) = (112, 92)
        self.haar_cascade = cv2.CascadeClassifier('haars/haarcascade_frontalface_default.xml')

    def setFrame(self, frame):
        self.frame = frame

    def preProcess(self):
        self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        self.mini = cv2.resize(self.gray, (self.gray.shape[1] / self.size, self.gray.shape[0] / self.size))


    def drawRectangle(self):
        faces = self.haar_cascade.detectMultiScale(self.mini)
        faces = sorted(faces, key=lambda x: x[3])
        if faces:
            face_i = faces[0]
            (x, y, w, h) = [v * self.size for v in face_i]
            face = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            cv2.rectangle(self.frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    def has(self):
        faces = self.haar_cascade.detectMultiScale(self.mini)
        faces = sorted(faces, key=lambda x: x[3])
        if faces:
            return True
        else:
            return False

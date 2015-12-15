import numpy as np
import cv2

from src.domain.center import Center
from src.hands.moviment import Moviment

# BUSCA OBJETOS QUE SE MOVIMENTA NO PLANO
# OS PARAMETROS DO CONSTRUTOR E UM CRITERIO DE  BUSCA
# Moviment(WIDTH%, MARGEM%, AREA_MINIMA, AREA_MAXIMA)

class DetectCascade(Moviment):
    def __init__(self, percW, percError=20, minArea=1000, maxArea=(1000 * 10)):
        Moviment.__init__(self, percW, percError, minArea, maxArea)
        DetectCascade.id = 0
        self.haar_cascade = cv2.CascadeClassifier('/home/william/git/hackerspace-opencv/experiments/totvs-2/data/cascade.xml')
        (self.im_width, self.im_height) = (112, 92)

    def setFrame(self, frame):
        self.frame = frame

    def preProcess(self):
        self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        mini = cv2.resize(self.gray, (self.gray.shape[1] / 4, self.gray.shape[0] / 4))
        faces = self.haar_cascade.detectMultiScale(mini, scaleFactor=4)
        self.faces = sorted(faces, key=lambda x: x[3])

    # RETORN UM ARRAY DE CENTROIDES
    # TIPO DO OBJ [Center]{x, y, w, h, id}
    # CADA VEZ QUE ENCONTRA UM OBJETO DA UM ID DIFERENTE
    def getCenters(self):
        self.centers = []
        if self.faces:
            for i in range(len(self.faces)):
                face_i = self.faces[i]
                (x, y, w, h) = [v * 4 for v in face_i]
                center = Center(x, y, w, h, DetectCascade.id)
                face = self.gray[y:y + h, x:x + w]
                face_resize = cv2.resize(face, (self.im_width, self.im_height))

                # cv2.rectangle(self.frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                self.centers.insert(0, center)
                DetectCascade.id += 1

        return self.centers

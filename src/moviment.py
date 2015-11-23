import numpy as np
import cv2

from src.center import Center

# BUSCA OBJETOS QUE SE MOVIMENTA NO PLANO
# OS PARAMETROS DO CONSTRUTOR E UM CRITERIO DE  BUSCA
# Moviment(WIDTH%, MARGEM%, AREA_MINIMA, AREA_MAXIMA)

class Moviment:
    def __init__(self, percW, percError=20, minArea=1000, maxArea=(1000 * 10)):
        Moviment.id = 0
        self.backgroundSubtractorKNN = cv2.createBackgroundSubtractorKNN()
        self.firstFrame = None
        self.minArea = minArea
        self.maxArea = maxArea
        self.percW = percW
        self.percError = percError
        Moviment.medianBlur = 11
        Moviment.threshold = 25
        Moviment.kernelVertical = 2
        Moviment.kernelHorizontal = 3
        Moviment.dilationInterator = 8
        Moviment.erodeInterator = 8
        Moviment.minArea = minArea
        Moviment.maxArea = maxArea

    def setFrame(self, frame):
        self.frame = frame

    def preProcess(self):

        if self.firstFrame ==  None:
                self.firstFrame = self.frame

        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

        #Gauss = cv2.GaussianBlur(gray, (5, 5), 0)
        self.MedianBlur = cv2.medianBlur(gray, Moviment.medianBlur)

        #aplica o BG Subtraction
        fgmask = self.backgroundSubtractorKNN.apply(self.MedianBlur)

        #binarizacao da imagem
        thresh = cv2.threshold(fgmask, Moviment.threshold, 255, cv2.THRESH_BINARY)[1]

        #o blur remove pequenos ruidos do background subtraction
        #MedianBlur = cv2.medianBlur(thresh, Moviment.medianBlur)

        #uso o recurso de dilatacao e erosao para unir todas as partes localizadas
        self.kernel = np.ones((Moviment.kernelVertical,Moviment.kernelHorizontal),np.uint8)
        self.dilation = cv2.dilate(thresh,self.kernel,iterations = Moviment.dilationInterator)
        self.erosion = cv2.erode(self.dilation,self.kernel,iterations = Moviment.erodeInterator)

    # RETORN UM ARRAY DE CENTROIDES
    # TIPO DO OBJ [Center]{x, y, w, h, id}
    # CADA VEZ QUE ENCONTRA UM OBJETO DA UM ID DIFERENTE
    def getCenters(self):
        (contours, a, _) = cv2.findContours(self.erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        self.centers = []

        for i in range(0, len(a)):
                x,y,w,h = cv2.boundingRect(a[i])
                if w*h > Moviment.minArea and w*h < Moviment.maxArea:
                    center = Center(x, y, w, h, Moviment.id)
                    percW, percY = center.getMetrica()

                    percWMax = self.percW + self.percError
                    percWMin = self.percW - self.percError
                    if percW != 0:
                        if percWMin > percW or percW > percWMax:
                            continue

                    self.centers.insert(0, center)

                    Moviment.id += 1
        return self.centers

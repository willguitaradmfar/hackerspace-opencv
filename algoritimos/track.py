import numpy as np
import cv2

from domain.center import Center

class Track:
    def __init__(self, minArea=1000, maxArea=(1000 * 10)):
        Track.id = 0
        self.backgroundSubtractorKNN = cv2.createBackgroundSubtractorKNN()
        self.firstFrame = None
        self.minArea = minArea
        self.maxArea = maxArea
        print("minArea: %s, maxArea: %s" % (self.minArea, self.maxArea))

    def setFrame(self, frame):
        self.frame = frame

    def preProcess(self):

        if self.firstFrame ==  None:
                self.firstFrame = self.frame

        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

        #Gauss = cv2.GaussianBlur(gray, (5, 5), 0)
        MedianBlur = cv2.medianBlur(gray, 11)

        #aplica o BG Subtraction
        fgmask = self.backgroundSubtractorKNN.apply(MedianBlur)

        #binarizacao da imagem
        thresh = cv2.threshold(fgmask, 25, 255, cv2.THRESH_BINARY)[1]

        #o blur remove pequenos ruidos do background subtraction
        MedianBlur = cv2.medianBlur(thresh, 11)

        #uso o recurso de dilatacao e erosao para unir todas as partes localizadas
        self.kernel = np.ones((5,5),np.uint8)
        self.dilation = cv2.dilate(thresh,self.kernel,iterations = 8)
        self.erosion = cv2.erode(self.dilation,self.kernel,iterations = 5)

    def getCenters(self):
        (contours, a, _) = cv2.findContours(self.erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        self.centers = [];
        for i in range(0, len(a)):
                if cv2.contourArea(a[i]) > self.minArea and cv2.contourArea(a[i]) < self.maxArea :
                        x,y,w,h = cv2.boundingRect(a[i])
                        self.centers.insert(0, Center(x, y, w, h, Track.id))
                Track.id += 1
        return self.centers

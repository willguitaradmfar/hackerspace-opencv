import numpy as np
import cv2

class Track:
    def __init__(self):
        self.backgroundSubtractorKNN = cv2.createBackgroundSubtractorKNN()
        self.firstFrame = None
        self.minArea = 1000

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

    def drawPoint(self):
        (contours, a, _) = cv2.findContours(self.erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for i in range(0, len(a)):
                if cv2.contourArea(a[i]) > self.minArea :
                        x,y,w,h = cv2.boundingRect(a[i])
                        cv2.circle(self.firstFrame,(x+(w/2),y+(h/2)), 3, (0,255,0))

    def drawPointPredicate(self, predicate):
        if predicate.has():
            (contours, a, _) = cv2.findContours(self.erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for i in range(0, len(a)):
                    if cv2.contourArea(a[i]) > self.minArea :
                            x,y,w,h = cv2.boundingRect(a[i])
                            cv2.circle(self.firstFrame,(x+(w/2),y+(h/2)), 5, (255,0,0))


    def drawRectangle(self):
        (contours, a, _) = cv2.findContours(self.erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for i in range(0, len(a)):
                if cv2.contourArea(a[i]) > self.minArea :
                        x,y,w,h = cv2.boundingRect(a[i])
                        cv2.rectangle(self.frame,(x,y),(x+w,y+h),(0,255,0),2)

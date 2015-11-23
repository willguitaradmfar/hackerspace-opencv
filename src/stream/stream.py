import numpy as np
import cv2

from src.hands.moviment import Moviment

from src.hands.identify import Identify

from src.hands.counterPoly import CounterPoly

from src.domain.label import Label

class Stream:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.polys = None
        self.channelBuffer = None

    def getFrame(self):
        ret, frame = self.cap.read()
        return frame

    def setChannelBuffer(self, channelBuffer):
        self.channelBuffer = channelBuffer

    def setConfig(self, config):
        self.config = config

    def finish(self):
        if self.channelBuffer != None:
            self.channelBuffer.thr.join()

        self.config.save()
        self.cap.release()
        cv2.destroyAllWindows()

    def setPolys(self, polys):
        self.polys = polys

    def play(self):

        moviment = Moviment(50, 50,100, (2 * 1000));

        identify = Identify(20)
        identify.setMoviment(moviment)

        counterPoly = CounterPoly()

        self.config.configure();

        cv2.namedWindow('frame', 2048)
        cv2.resizeWindow("frame", 1024, 768)

        cv2.namedWindow('dilation', 2048)
        cv2.resizeWindow("dilation", 1024, 768)

        cv2.namedWindow('erosao', 2048)
        cv2.resizeWindow("erosao", 1024, 768)

        cv2.namedWindow('gauss', 2048)
        cv2.resizeWindow("gauss", 1024, 768)

        cv2.namedWindow('borda', 2048)
        cv2.resizeWindow("borda", 1024, 768)

        cv2.createTrackbar("Gauss", "gauss", self.config.medianBlur, 25, self.config.gaussCallback)
        cv2.createTrackbar("Vertical", "dilation", self.config.kernelVertical, 15, self.config.verticalCallback)
        cv2.createTrackbar("Horizontal", "dilation", self.config.kernelHorizontal, 15, self.config.horizontalCallback)
        cv2.createTrackbar("Dilation", "dilation", self.config.dilationInterator, 15, self.config.dilationCallback)
        cv2.createTrackbar("Erode", "erosao", self.config.erodeInterator, 15, self.config.erodeCallback)
        cv2.createTrackbar("Deslocamento Max.", "frame", self.config.deslocamentoMax, 100, self.config.velocidadeCallback)
        cv2.createTrackbar("Area Minima", "frame", self.config.minArea, 20000, self.config.minAreaCallback)
        cv2.createTrackbar("Area Maxima", "frame", self.config.maxArea, 200000, self.config.maxAreaCallback)
        cv2.createTrackbar("Velocidade do Video", "frame", self.config.modFrames, 15, self.config.modFramesCallback)

        count = 0
        cframe = 0

        while(True):

            frame = self.getFrame()

            if count < 15:
                count += 1
                continue

            cframe += 1;

            if cframe % self.config.modFrames != 0:
                continue

            moviment.setFrame(frame)
            moviment.preProcess()
            cv2.imshow('erosao', moviment.erosion)


            centers = identify.getPointsMap(self.polys)

            if self.polys != None:
                counterPoly.setCenters(centers)

                for poly in self.polys:
                    try:
                        label = Label(["%s: %s" % (poly.name, counterPoly.areas[poly.name])])
                        label.setFrame(frame)
                        poly.setLabel(label)
                    except:
                        label = Label(["%s: %s" % (poly.name, 0)])
                        label.setFrame(frame)
                        poly.setLabel(label)

                for poly in self.polys:
                    poly.setFrame(frame)
                    poly.draw()

            if self.channelBuffer != None:
                self.channelBuffer.setFrame(frame)

            cv2.imshow('frame', frame)
            cv2.imshow('gauss', moviment.MedianBlur)
            cv2.imshow('dilation', moviment.dilation)
            cv2.imshow('borda', moviment.erosion)

            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break

        self.finish()

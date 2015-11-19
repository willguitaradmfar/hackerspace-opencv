import numpy as np
import cv2

from stream.video import Video
from stream.cam import Cam

from algoritimos.moviment import Moviment
from algoritimos.face import Face
from algoritimos.identify import Identify

from domain.polygon import Polygon
from domain.line import Line
from domain.point import Point
from domain.counterPoly import CounterPoly

from domain.label import Label

arrayPoly = []

poly = Polygon()
poly.setName("Subiu")

poly.addLine(Line(Point(0, 0), Point(0,220)))
poly.addLine(Line(Point(0,220), Point(450,120)))
poly.addLine(Line(Point(450,120), Point(450,0)))
poly.addLine(Line(Point(450,0), Point(0,0)))


arrayPoly.insert(0, poly)

poly = Polygon()
poly.setName("Desceu")
poly.addLine(Line(Point(0,220), Point(450,120)));
poly.addLine(Line(Point(450,120), Point(620,170)));
poly.addLine(Line(Point(620,170), Point(250,450)));
poly.addLine(Line(Point(100,450), Point(0,220)));
arrayPoly.insert(0, poly)

counterPoly = CounterPoly()


moviment = Moviment(50, 50,100, (50 * 1000));

stream = Video('videos/videoContagem.mp4');

identify = Identify(23)
identify.setMoviment(moviment)

count = 0

counter = dict()

def threshCallback(value):
    Moviment.threshold = value
    return

def gaussCallback(value):
    try:
        if value % 2 == 0:
            value -= 1
        if value <= 0:
            value = 1
                    
        Moviment.medianBlur = value
    except:
        return

def verticalCallback(value):
    Moviment.kernelVertical = value
    return

def horizontalCallback(value):
    Moviment.kernelHorizontal = value
    return

def dilationCallback(value):
    Moviment.dilationInterator = value
    return

def erodeCallback(value):
    Moviment.erodeInterator = value
    return


cv2.namedWindow('frame')
cv2.namedWindow('dilation')
cv2.namedWindow('erosao')
cv2.namedWindow('gauss')
cv2.createTrackbar("Threshold", "frame", Moviment.threshold, 255, threshCallback)
cv2.createTrackbar("Gauss", "gauss", Moviment.medianBlur, 25, gaussCallback)
cv2.createTrackbar("Vertical", "dilation", Moviment.kernelVertical, 15, verticalCallback)
cv2.createTrackbar("Horizontal", "dilation", Moviment.kernelHorizontal, 15, horizontalCallback)
cv2.createTrackbar("Dilation", "dilation", Moviment.dilationInterator, 15, dilationCallback)
cv2.createTrackbar("Erode", "erosao", Moviment.erodeInterator, 15, erodeCallback)

while(True):

    frame = stream.getFrame()

    if count < 15:
        count += 1
        continue

    for poly in arrayPoly:
        poly.setFrame(frame)
        poly.draw()

    moviment.setFrame(frame)
    moviment.preProcess()
    cv2.imshow('erosao', moviment.erosion)

    centers = identify.getPointsMap(arrayPoly)
    counterPoly.setCenters(centers)

    for poly in arrayPoly:
        try:
            label = Label(["%s: %s" % (poly.name, counterPoly.areas[poly.name])])
            label.setFrame(frame)
            poly.setLabel(label)
        except:
            label = Label(["%s: %s" % (poly.name, 0)])
            label.setFrame(frame)
            poly.setLabel(label)


    cv2.imshow('frame', frame)
    cv2.imshow('gauss', moviment.MedianBlur)
    cv2.imshow('dilation', moviment.dilation)
    cv2.imshow('borda', moviment.erosion)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


stream.finish()
cv2.destroyAllWindows()


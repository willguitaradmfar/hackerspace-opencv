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
poly.setName("Entrada")
poly.addLine(Line(Point(0,0), Point(250,0)))
poly.addLine(Line(Point(250,0), Point(250,450)))
poly.addLine(Line(Point(250,450), Point(0,450)))
poly.addLine(Line(Point(0, 450), Point(0,0)))
arrayPoly.insert(0, poly)

poly = Polygon()
poly.setName("UX")
poly.addLine(Line(Point(250,0), Point(500,0)));
poly.addLine(Line(Point(500,0), Point(500,450)));
poly.addLine(Line(Point(500,450), Point(250,450)));
poly.addLine(Line(Point(250,450), Point(250,0)));
arrayPoly.insert(0, poly)

counterPoly = CounterPoly()


moviment = Moviment(50, 50,500, (100 * 1000));

stream = Video('videos/videoContagem.mp4');

identify = Identify(60)
identify.setMoviment(moviment)

count = 0

counter = dict()

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

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


stream.finish()
cv2.destroyAllWindows()

import numpy as np
import cv2

from stream.video import Video
from stream.cam import Cam

from algoritimos.track import Track
from algoritimos.face import Face
from algoritimos.identify import Identify

from domain.polygon import Polygon
from domain.line import Line
from domain.point import Point

dictPoly = dict()

poly1 = Polygon();
line1 = Line(Point(0,0), Point(0,430))
line2 = Line(Point(0,430), Point(1250,480))
line3 = Line(Point(1250,480), Point(1250,0))
line4 = Line(Point(1250,0), Point(0,0))
poly1.addLine(line1);
poly1.addLine(line2);
poly1.addLine(line3);
poly1.addLine(line4);

dictPoly['Fora'] = poly1

poly2 = Polygon();
l1 = Line(Point(0,430), Point(1255,480))
l2 = Line(Point(1255,480), Point(1255,715))
l3 = Line(Point(1255,715), Point(0,715))
l4 = Line(Point(0,715), Point(0,470))
poly2.addLine(l1);
poly2.addLine(l2);
poly2.addLine(l3);
poly2.addLine(l4);

dictPoly['Dentro'] = poly2


track = Track(1000, (100 * 1000));

stream = Cam();

identifyMoviment = Identify(60)
identifyMoviment.setTrack(track)

count = 0

while(True):

    frame = stream.getFrame()

    if count < 100:
        count += 1
        continue

    poly1.setFrame(frame)
    poly1.draw()

    poly2.setFrame(frame)
    poly2.draw()

    track.setFrame(frame)
    track.preProcess()

    identifyMoviment.getPointsMap(dictPoly)
    cv2.imshow('frame', frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


stream.finish()
cv2.destroyAllWindows()

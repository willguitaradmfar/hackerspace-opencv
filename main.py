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
from domain.stateManager import StateManager

dictPoly = dict()

poly1 = Polygon();
line1 = Line(Point(0,0), Point(250,0))
line2 = Line(Point(250,0), Point(250,450))
line3 = Line(Point(250,450), Point(0,450))
line4 = Line(Point(0, 450), Point(0,0))
poly1.addLine(line1);
poly1.addLine(line2);
poly1.addLine(line3);
poly1.addLine(line4);

dictPoly['Cadeiras'] = poly1

poly2 = Polygon();
l1 = Line(Point(250,0), Point(500,0))
l2 = Line(Point(500,0), Point(500,450))
l3 = Line(Point(500,450), Point(250,450))
l4 = Line(Point(250,450), Point(250,0))
poly2.addLine(l1);
poly2.addLine(l2);
poly2.addLine(l3);
poly2.addLine(l4);

dictPoly['Biblioteca'] = poly2


stateManager = StateManager()


track = Track(1000, (100 * 1000));

stream = Cam();

identify = Identify(60)
identify.setTrack(track)

count = 0

counter = dict()

while(True):

    frame = stream.getFrame()

    if count < 15:
        count += 1
        continue

    poly1.setFrame(frame)
    poly1.draw()

    poly2.setFrame(frame)
    poly2.draw()

    track.setFrame(frame)
    track.preProcess()

    centers = identify.getPointsMap(dictPoly)

    stateManager.setCenters(centers)

    print(stateManager.areas)

    cv2.imshow('frame', frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


stream.finish()
cv2.destroyAllWindows()

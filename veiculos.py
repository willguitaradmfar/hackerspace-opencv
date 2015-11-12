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
line1 = Line(Point(0,0), Point(120,0))
line2 = Line(Point(120,0), Point(220,200))
line3 = Line(Point(220,200), Point(0,200))
line4 = Line(Point(0,200), Point(0,0))
poly1.addLine(line1);
poly1.addLine(line2);
poly1.addLine(line3);
poly1.addLine(line4);

dictPoly['Zebra'] = poly1

track = Track(1000, (10 * 1000));

stream = Video("videos/videoVeiculos.mp4");

identify = Identify(30)
identify.setTrack(track)

while(True):

    frame = stream.getFrame()

    poly1.setFrame(frame)
    poly1.draw()

    track.setFrame(frame)
    track.preProcess()

    identify.getPointsMap(dictPoly)
    cv2.imshow('frame', frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


stream.finish()
cv2.destroyAllWindows()

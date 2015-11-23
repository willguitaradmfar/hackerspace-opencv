import numpy as np
import cv2

from src.video import Video

from src.polygon import Polygon
from src.line import Line
from src.point import Point
from src.configCam import ConfigCam

arrayPoly = []

poly = Polygon()
poly.setName("Subiu")
poly.addLine(Line(Point(0, 0), Point(0,0)))
poly.addLine(Line(Point(0,0), Point(0,0)))
poly.addLine(Line(Point(0,0), Point(0,0)))
poly.addLine(Line(Point(0,0), Point(0,0)))
arrayPoly.insert(0, poly)

stream = Video('videos/japao.mp4');
stream.setConfig(ConfigCam())
stream.setPolys(arrayPoly)
stream.play()

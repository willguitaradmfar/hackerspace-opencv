import numpy as np
import cv2

from src.stream.video import Video

from src.domain.polygon import Polygon
from src.domain.line import Line
from src.domain.point import Point
from src.config.configCam import ConfigCam

arrayPoly = []

poly = Polygon()
poly.setName("Subiu")
poly.addLine(Line(Point(0, 0), Point(0,0)))
poly.addLine(Line(Point(0,0), Point(0,0)))
poly.addLine(Line(Point(0,0), Point(0,0)))
poly.addLine(Line(Point(0,0), Point(0,0)))
arrayPoly.insert(0, poly)

stream = Video('videos/videoContagem.mp4');
stream.setConfig(ConfigCam())
stream.setPolys(arrayPoly)
stream.play()

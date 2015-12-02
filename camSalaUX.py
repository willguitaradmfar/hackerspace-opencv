import numpy as np
import cv2

from src.stream.video import Video

from src.domain.polygon import Polygon
from src.domain.line import Line
from src.domain.point import Point
from src.config.configCam import ConfigCam

from src.channelBuffer.channelBufferMqtt import ChannelBufferMqtt

arrayPoly = []



_array = [[[217, 74], [244, 457]], [[244, 457], [73, 462]], [[73, 462], [42, 78]], [[42, 78], [219, 77]]]


arrayPoly = []

poly = Polygon()
poly.setName("ForaDaFaixa")

arrayPoly.insert(0, poly)

for i in _array:
    poly.addLine(Line(Point(i[0][0],i[0][1]), Point(i[1][0],i[1][1])))


channelBuffer = ChannelBufferMqtt()

stream = Video('videos/videoSalaUX.webm');
stream.setConfig(ConfigCam())
stream.setPolys(arrayPoly)
stream.setChannelBuffer(channelBuffer)
stream.play()

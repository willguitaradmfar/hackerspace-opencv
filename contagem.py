import numpy as np
import cv2
import json

from src.stream.video import Video

from src.domain.polygon import Polygon
from src.domain.line import Line
from src.domain.point import Point
from src.config.configCam import ConfigCam

from src.channelBuffer.channelBufferMqtt import ChannelBufferMqtt

channelBuffer = ChannelBufferMqtt()

_array = [[[80, 81], [128, 79]], [[128, 79], [190, 137]], [[190, 137], [118, 149]], [[118, 149], [79, 79]]]


arrayPoly = []

poly = Polygon()
poly.setName("ForaDaFaixa")

arrayPoly.insert(0, poly)

for i in _array:
    poly.addLine(Line(Point(i[0][0],i[0][1]), Point(i[1][0],i[1][1])))

stream = Video('videos/videoContagem.mp4');
stream.setConfig(ConfigCam())
stream.setPolys(arrayPoly)
stream.setChannelBuffer(channelBuffer)
stream.play()

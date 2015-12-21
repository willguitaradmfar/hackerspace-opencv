import numpy as np
import cv2

from src.stream.video import Video
from src.stream.cam import Cam

from src.domain.polygon import Polygon
from src.domain.line import Line
from src.domain.point import Point
from src.config.configCam import ConfigCam

from src.channelBuffer.channelBufferMqtt import ChannelBufferMqtt


_array = [[[188, 238], [723, 260]], [[723, 260], [507, 350]], [[507, 350], [316, 351]], [[316, 351], [187, 239]]]

_arrayD = [[[348, 205], [599, 214]], [[599, 214], [603, 247]], [[603, 247], [280, 234]], [[280, 234], [348, 205]]]

arrayPoly = []

poly = Polygon()
poly.setName("ForaDaFaixa")

polyD = Polygon()
polyD.setName("Faixa")

arrayPoly.insert(0, poly)
arrayPoly.insert(0, polyD)

for i in _array:
    poly.addLine(Line(Point(i[0][0],i[0][1]), Point(i[1][0],i[1][1])))

for i in _arrayD:
    polyD.addLine(Line(Point(i[0][0],i[0][1]), Point(i[1][0],i[1][1])))

channelBuffer = ChannelBufferMqtt()

stream = Video("videos/japao.mp4");
stream.setConfig(ConfigCam())
stream.setPolys(arrayPoly)
stream.setChannelBuffer(channelBuffer)
stream.play()

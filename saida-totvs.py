import numpy as np
import cv2

from src.stream.video import Video
from src.stream.cam import Cam

from src.domain.polygon import Polygon
from src.domain.line import Line
from src.domain.point import Point
from src.config.configCam import ConfigCam

from src.channelBuffer.channelBufferMqtt import ChannelBufferMqtt


_array = [[[579, 506], [1038, 516]], [[1038, 516], [681, 715]], [[681, 715], [434, 713]], [[434, 713], [253, 475]], [[253, 475], [580, 506]]]

arrayPoly = []

poly = Polygon()
poly.setName("ForaDaFaixa")

arrayPoly.insert(0, poly)

for i in _array:
    poly.addLine(Line(Point(i[0][0],i[0][1]), Point(i[1][0],i[1][1])))

channelBuffer = ChannelBufferMqtt()

stream = Video("videos/saida-totvs.mp4");
stream.setConfig(ConfigCam("saida-totvs.conf"))
stream.setPolys(arrayPoly)
stream.setChannelBuffer(channelBuffer)
stream.play()

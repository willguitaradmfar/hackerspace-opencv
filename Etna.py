import numpy as np
import cv2

from src.stream.video import Video

from src.domain.polygon import Polygon
from src.domain.line import Line
from src.domain.point import Point
from src.config.configCam import ConfigCam

from src.channelBuffer.channelBufferVoid import ChannelBufferVoid

arrayPoly = []

polyOff = Polygon()
polyOff.setName("Fora")
polyOff.setClass("off")
#Point(Coluna, Linha)
polyOff.addLine(Line(Point(1, 400), Point(370, 400)))
polyOff.addLine(Line(Point(370, 400), Point(900, 680)))
polyOff.addLine(Line(Point(900, 680), Point(1030, 680)))
polyOff.addLine(Line(Point(1030, 680), Point(1030, 1)))
polyOff.addLine(Line(Point(1030, 1), Point(1, 1)))
polyOff.addLine(Line(Point(1, 1), Point(1, 400)))
arrayPoly.insert(0, polyOff)

polyLine = Polygon()
polyLine.setName("Fila")
polyLine.setClass("line")
#Point(Coluna, Linha)
polyLine.addLine(Line(Point(140, 410), Point(340, 400)))
polyLine.addLine(Line(Point(340, 400), Point(750, 680)))
polyLine.addLine(Line(Point(750, 680), Point(200, 680)))
polyLine.addLine(Line(Point(200, 680), Point(140, 410)))
arrayPoly.insert(0, polyLine)

channelBuffer = ChannelBufferVoid()

stream = Video("videos/Etna/ice_video_20160126-135019.webm");
stream.setConfig(ConfigCam())
stream.setPolys(arrayPoly)
stream.setChannelBuffer(channelBuffer)
stream.play()

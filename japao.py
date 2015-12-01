import numpy as np
import cv2

from src.stream.video import Video

from src.domain.polygon import Polygon
from src.domain.line import Line
from src.domain.point import Point
from src.config.configCam import ConfigCam

from src.channelBuffer.channelBufferMqtt import ChannelBufferMqtt


channelBuffer = ChannelBufferMqtt()

stream = Video('videos/japao.mp4');
stream.setConfig(ConfigCam())
stream.setChannelBuffer(channelBuffer)
stream.play()

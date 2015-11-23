import numpy as np
import cv2

from src.video import Video

from src.polygon import Polygon
from src.line import Line
from src.point import Point
from src.configCam import ConfigCam

stream = Video('videos/japao.mp4');
stream.setConfig(ConfigCam())
stream.play()

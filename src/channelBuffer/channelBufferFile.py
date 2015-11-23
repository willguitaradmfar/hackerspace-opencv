import cv2
import threading

from src.channelBuffer.channelBuffer import ChannelBuffer

class ChannelBufferFile(ChannelBuffer):
    def __init__(self):
        ChannelBuffer.__init__(self)

    def run(self):
        cv2.imwrite("/tmp/face-default.jpg", self.frame)

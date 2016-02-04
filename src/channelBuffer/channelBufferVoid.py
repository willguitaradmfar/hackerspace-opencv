import cv2
import threading

from src.channelBuffer.channelBuffer import ChannelBuffer

class ChannelBufferVoid(ChannelBuffer):
    def __init__(self):
        ChannelBuffer.__init__(self)
        self.cacheCounterPoly = ""

    def run(self):
        pass
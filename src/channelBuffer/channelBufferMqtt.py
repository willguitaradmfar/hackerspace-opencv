import cv2
import threading
import base64

import paho.mqtt.client as paho

client = paho.Client()

client.connect("127.0.0.1", 1884, 60)

from src.channelBuffer.channelBuffer import ChannelBuffer

class ChannelBufferMqtt(ChannelBuffer):
    def __init__(self):
        ChannelBuffer.__init__(self)

    def run(self):
        b64 = base64.encodestring(cv2.imencode('.png',self.frame)[1])
        client.publish("frame", b64)

        client.publish("counterPoly", counterPoly.areas)

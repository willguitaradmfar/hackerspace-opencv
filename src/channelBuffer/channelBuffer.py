import cv2
import threading

class ChannelBuffer:
    def __init__(self):
        return

    def run(self):
        print('Nao deve fazer nada')

    def setFrame(self, frame):
        self.frame = frame
        self.thr = threading.Thread(target=self.run, args=(), kwargs={})
        self.thr.start()

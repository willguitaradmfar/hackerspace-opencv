import cv2
import threading

class ChannelBuffer:
    def __init__(self):
        return

    def run(self):
        print('Nao deve fazer nada')

    def setFrame(self, frame, counterPoly):
        self.frame = frame
        self.counterPoly = counterPoly
        self.thr = threading.Thread(target=self.run, args=(), kwargs={})
        self.thr.start()

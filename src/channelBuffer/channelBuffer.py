import cv2
import threading

class ChannelBuffer:
    def __init__(self):
        self.centers = []
        

    def run(self):
        print('Nao deve fazer nada')

    def setFrame(self, frame, counterPoly, centers):
        self.frame = frame
        self.centers = centers
        self.counterPoly = counterPoly
        self.thr = threading.Thread(target=self.run, args=(), kwargs={})
        self.thr.start()

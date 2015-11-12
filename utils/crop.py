import numpy as np
import math

class Crop:
    def __init__(self):
        return

    def crop(self, frame, (x, y, w, h)):
        return frame[x:y, w:h]

import numpy as np
import cv2

class Label:
    def __init__(self, frame, box, texts):
        self.colorFont = (255,255,0)
        for i in range(0, len(texts)):
            text = texts[i]
            cv2.putText(frame, text, (box.x+box.w+2, box.y+10+(i*15)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, self.colorFont, 1)

'''
    http://docs.opencv.org/master/db/d5c/tutorial_py_bg_subtraction.html#gsc.tab=0
'''
import numpy as np
import cv2

from algoritimos.track import Track
from algoritimos.face import Face

track = Track();

face = Face();

cap = cv2.VideoCapture(0)

count = 0
while(True):
        if count == 5:
                ret, frame = cap.read()

                track.setFrame(frame);
                face.setFrame(frame);

                track.preProcess()
                face.preProcess()



                track.drawPoint()
                track.drawRectangle()
                track.drawPointPredicate(face);

                face.drawRectangle();

                #exibo as imagens
                cv2.imshow('mark', track.erosion)
                cv2.imshow('frame', track.frame)
                cv2.imshow('flow', track.firstFrame)

                k = cv2.waitKey(30) & 0xff
                if k == 27:
                    break
        else:
                count += 1

cap.release()
cv2.destroyAllWindows()

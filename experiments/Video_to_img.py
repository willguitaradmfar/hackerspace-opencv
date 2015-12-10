'''
    http://docs.opencv.org/master/db/d5c/tutorial_py_bg_subtraction.html#gsc.tab=0
'''
import numpy as np
import cv2

numero = 1

cap = cv2.VideoCapture("C:\hackerspace-opencv\experiments\object-marker\saida-totvs.mp4")
count = 0
while(True):
        
        ret, frame = cap.read()
        cv2.imshow('Video', frame)

        k = cv2.waitKey(30) & 0xff

        if k == 116:
                cv2.imwrite("C:\hackerspace-opencv\experiments\imgs\img"+str(numero)+".png", frame)
                numero += 1
                
        if k == 27:
                break
        

cap.release()
cv2.destroyAllWindows()

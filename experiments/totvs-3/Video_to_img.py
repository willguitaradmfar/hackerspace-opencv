import numpy as np
import cv2

numero = 1

cap = cv2.VideoCapture("/home/william/Desktop/VID_20151214_180050848.mp4")
count = 0

cv2.namedWindow('Video', 2048)
cv2.resizeWindow("Video", 1024, 768)

while(True):

        ret, frame = cap.read()
        cv2.imshow('Video', frame)

        k = cv2.waitKey(30) & 0xff

        if k == 116:
                cv2.imwrite("pos/img"+str(numero)+".png", frame)
                numero += 1

        if k == 27:
                break


cap.release()
cv2.destroyAllWindows()

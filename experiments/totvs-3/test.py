# train.py
import cv2, sys, numpy, os
size = 4
fn_haar = 'HS.xml'

(im_width, im_height) = (112, 92)
haar_cascade = cv2.CascadeClassifier(fn_haar)
webcam = cv2.VideoCapture(0)

# The program loops until it has 20 images of the face.

cv2.namedWindow('OpenCV', 2048)
cv2.resizeWindow("OpenCV", 1024, 768)

while True:
    (rval, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    mini = cv2.resize(gray, (gray.shape[1] / size, gray.shape[0] / size))
    faces = haar_cascade.detectMultiScale(mini)
    faces = sorted(faces, key=lambda x: x[3])
    if faces:
        for i in range(len(faces)):
            face_i = faces[i]
            (x, y, w, h) = [v * size for v in face_i]
            face = gray[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (im_width, im_height))

            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)


    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(30) & 0xFF
    if key == 27:
        break

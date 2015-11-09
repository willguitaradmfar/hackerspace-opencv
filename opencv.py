# facerec.py
import cv2, sys, numpy, os
size = 4
fn_haar = 'haars/haarcascade_frontalface_default.xml'
fn_dir = 'att_faces'

# Part 1: Create fisherRecognizer
print('Training...')
# Create a list of images and a list of corresponding names
(images, lables, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(fn_dir):
    for subdir in dirs:
        #print(id)
        names[id] = subdir
        subjectpath = os.path.join(fn_dir, subdir)
        print(subdir)
        for filename in os.listdir(subjectpath):
            names[id] = subdir
            path = subjectpath + '/' + filename
            lable = id
            images.append(cv2.imread(path, 0))
            lables.append(int(lable))
            id += 1
(im_width, im_height) = (112, 92)

# Create a Numpy array from the two lists above
(images, lables) = [numpy.array(lis) for lis in [images, lables]]

# OpenCV trains a model from the images

try:
    model = cv2.createLBPHFaceRecognizer()
    model.train(images, lables)
except ImportError, AttributeError:
    print("Fisher Recognizer is supported by OpenCV >= 2.4.4")



# Part 2: Use fisherRecognizer on camera stream
haar_cascade = cv2.CascadeClassifier(fn_haar)

webcam = cv2.VideoCapture(0)
#webcam = cv2.VideoCapture('video/v1.mp4')

while True:
    (rval, frame) = webcam.read()
    frame=cv2.flip(frame,1,0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mini = cv2.resize(gray, (gray.shape[1] / size, gray.shape[0] / size))
    faces = haar_cascade.detectMultiScale(mini)
    for i in range(len(faces)):
        face_i = faces[i]
        (x, y, w, h) = [v * size for v in face_i]
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (im_width, im_height))

        # Try to recognize the face
        prediction = model.predict(face_resize)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        # cv2.putText(frame,
        #     '%s - %.0f' % (names[prediction[0]],prediction[1]),
        #     (x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))

        if prediction[1] < 80:
          cv2.putText(frame,
              '%s - %.0f' % (names[prediction[0]],prediction[1]),
              (x-10, y-10), cv2.FONT_HERSHEY_PLAIN,2,(255, 255, 255))
        else:
          cv2.putText(frame,
              'Unknown (%s) - %.0f' % (names[prediction[0]], prediction[1]),
              (x-10, y-10), cv2.FONT_HERSHEY_PLAIN,2,(255, 255, 0))

    cv2.imshow('OpenCV', frame)
    key = cv2.waitKey(10)
    if key == 27:
        break

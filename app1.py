import cv2
import sys

cascPath = "haars/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

#Valor que  o algoritmo vai desconciderar para fazer a identificacao do movimento
#Obs: neste caso terei apenas 1 ponto para comparar, por isso coloquei um valos absurdo
ErroPadrao = 1000

#Determina o fator de distancia, isso sera levado em consideracao para determinar
#se eh um ponto em movimento ou um outro ponto aleatorio
FatorDeDistancia = 50

#Guarda as coordenadas dos pontos adiquiridos
#neste caso vou guardar apenas 2
pontos = []

def module(number):
    if number < 0:
        number = number * -1
    return number

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
   # frame = cv2.flip(frame,0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.circle(frame,(x+(w/2),y+(h/2)), 3, (0,255,0))

        pontos.insert(0, [(x+(w/2)), (y+(h/2))])
        
        if len(pontos) > 2:
            pontos.pop()
            
            distx = module(pontos[0][0] - pontos[1][0])
            disty = module(pontos[0][1] - pontos[1][1])
            
            if distx < ErroPadrao and disty < ErroPadrao:
                if pontos[0][0] - pontos[1][0] < 0 and (pontos[0][1] - pontos[1][1] >= -10 and pontos[0][1] - pontos[1][1] <= 10):
                    cv2.putText(frame, "Direita", (x+(w/2),y+(h/2)), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
                if pontos[0][0] - pontos[1][0] > 0 and (pontos[0][1] - pontos[1][1] >= -10 and pontos[0][1] - pontos[1][1] <= 10):
                    cv2.putText(frame, "Esquerda", (x+(w/2),y+(h/2)), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
            
            
        
    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

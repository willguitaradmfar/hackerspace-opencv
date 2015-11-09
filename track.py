'''
    http://docs.opencv.org/master/db/d5c/tutorial_py_bg_subtraction.html#gsc.tab=0
'''
import numpy as np
import cv2

#funcao para o sort
def getKey(item):
        return item[0]

cap = cv2.VideoCapture(0)
#o BG subtraction KNN funcionou melhor nos meus testes
#fgbg = cv2.createBackgroundSubtractorMOG2()
fgbg = cv2.createBackgroundSubtractorKNN()

firstFrame = None
count = 0
while(True):
        if count == 15:
                ret, frame = cap.read()
                frame = cv2.flip(frame,0)

                if firstFrame ==  None:
                        firstFrame = frame
                
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                
                #Gauss = cv2.GaussianBlur(gray, (5, 5), 0)
                MedianBlur = cv2.medianBlur(gray, 11)
                        
                #aplica o BG Subtraction
                fgmask = fgbg.apply(MedianBlur)

                #binarizacao da imagem
                thresh = cv2.threshold(fgmask, 25, 255, cv2.THRESH_BINARY)[1]

                #o blur remove pequenos ruidos do background subtraction
                MedianBlur = cv2.medianBlur(thresh, 11)

                #uso o recurso de dilatacao e erosao para unir todas as partes localizadas
                kernel = np.ones((5,5),np.uint8)
                dilation = cv2.dilate(thresh,kernel,iterations = 8)
                erosion = cv2.erode(dilation,kernel,iterations = 5)

                #Com o Canny consigo fazer a aquisicao das bordas muito melhor
                #sem o canny o findContours encontra apenas a borda de um dos lados da imagem
                #isso eh bom e ruim, pois se a imagem estiver cortada em cima e em baixo, com o canny, ele considera dois objetos
                #edges = cv2.Canny(erosion,50,100)
                (contours, a, _) = cv2.findContours(erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                #determino uma area minima para aquisicao, evitando pegar pequenos ruidos
                minArea = 1000
                for i in range(0, len(a)):
                        if cv2.contourArea(a[i]) > minArea :
                                # calcula area do contorno
                                maxsize = cv2.contourArea(a[i])
                                x,y,w,h = cv2.boundingRect(a[i])

                                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)        
                                cv2.circle(firstFrame,(x+(w/2),y+(h/2)), 3, (0,255,0))
                       
                #exibo as imagens
                cv2.imshow('mark', erosion)
                cv2.imshow('frame', frame)
                cv2.imshow('flow', firstFrame)
                k = cv2.waitKey(30) & 0xff
                if k == 27:
                    break
        else:
                count += 1

cap.release()
cv2.destroyAllWindows()

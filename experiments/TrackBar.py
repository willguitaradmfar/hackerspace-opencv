'''
    http://docs.opencv.org/master/db/d5c/tutorial_py_bg_subtraction.html#gsc.tab=0
'''
import numpy as np
import cv2

class test:

    def __init__(self):
        self.gauss = 1
        self.thresh1 = 25
        self.thresh2 = 255
        return
    
    def callback_gauss(self, value):
        try:
            if value % 2 == 0:
                value -= 1
            if value <= 0:
                value = 1
                
            self.gauss = value
        except:
            return

    def callback_thresh1(self, value):
        try:  
            self.thresh1 = value
        except:
            return

    def callback_thresh2(self, value):
        try: 
            self.thresh2 = value
        except:
            return

        

    def procces(self):
        cap = cv2.VideoCapture(0)
        #o BG subtraction KNN funcionou melhor nos meus testes
        #fgbg = cv2.createBackgroundSubtractorMOG2()
        fgbg = cv2.createBackgroundSubtractorKNN()

        firstFrame = None
        count = 0

        aaa = np.zeros((300,512,3), np.uint8)
        cv2.namedWindow('slider')
        cv2.createTrackbar("Gauss", "slider", 1, 25, self.callback_gauss)
        cv2.createTrackbar("thresh1", "slider", 1, 255, self.callback_thresh1)
        cv2.createTrackbar("thresh2", "slider", 1, 255, self.callback_thresh2)

        while(True):
                #Como o obturador das cameras demora um pouco para se adaptar espero a aquisicao de alguns frames
                #antes de comecar o processamento das imagens
                if count == 15:
                        ret, frame = cap.read()
                        #Nao sei pq minha webcam pegava a imagem invertida
                        #Se ficar de ponta cabeca remova essa linha
                        frame = cv2.flip(frame,0)
                        
                        #Defino o primeiro frame como o demonstrativo para o Heat Map
                        if firstFrame ==  None:
                                firstFrame = frame
                        
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        
                        #Existem algumas opcoes de filtro passa-baixo, estou utilziando a MedianBlur pois esse metodo
                        #preserva as bordas da imagem ao contrario do GaussianBlur
                        Gauss = cv2.GaussianBlur(gray, (self.gauss, self.gauss), 0)

                        thresh = cv2.threshold(Gauss, self.thresh1, self.thresh2, cv2.THRESH_BINARY)[1]
                        
                        cv2.imshow("slider", Gauss)
                        cv2.imshow("thresh", thresh)
                        k = cv2.waitKey(30) & 0xff
                        if k == 27:
                            break
                else:
                        count += 1

        cap.release()
        cv2.destroyAllWindows()

a = test()
a.procces()

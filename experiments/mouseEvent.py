import cv2
import numpy as np



class mouseTest():

    def __init__(self):
        self.points = []
        self.lines = []
        self.memoryx = []
        self.memoryy = []
        self.count = 0
        self.firstPoint = []
    # mouse callback function
    def lineCallback(self,event,x,y,flags,param):
        
        if event == cv2.EVENT_LBUTTONUP:
            #cv2.circle(img,(x,y),100,(255,0,0),-1)

            print(len(self.points))
            if len(self.points) < 2:
                if self.count >= 2:
                    self.points.append([self.memoryx,self.memoryy])
                self.count += 1
                self.points.append([x,y])
                if len(self.firstPoint) == 0:
                    self.firstPoint.append(x)
                    self.firstPoint.append(y)
                self.memoryx = x
                self.memoryy = y
            if len(self.points) >= 2:
                self.lines.append([self.points[0],self.points[1]])
                self.points = []
            print(self.lines)

    def verifyLastPoint(self):
        total = len(self.lines)-1
        if len(self.lines) > 1:
            lastX = self.lines[total][1][0]
            lastY = self.lines[total][1][1]
            if lastX <= self.firstPoint[0]+2 and lastX >= self.firstPoint[0]-2 and lastY <= self.firstPoint[1]+2 and lastY >= self.firstPoint[1]-2:
                print("Fechou")
                self.points = []
                self.lines = []
                self.memoryx = []
                self.memoryy = []
                self.count = 0
                self.firstPoint = []
           
    def run(self):
        # Create a black image, a window and bind the function to window
        img = np.zeros((512,512,3), np.uint8)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.lineCallback)

        while(1):

            for line in self.lines:
                cv2.line(img,(line[0][0], line[0][1]),(line[1][0], line[1][1]),(255,0,0),3)

            self.verifyLastPoint()
            
            cv2.imshow('image',img)
            k = cv2.waitKey(20) & 0xFF
            if k == 27:
                break
            elif k == ord('a'):
                print ix,iy
        cv2.destroyAllWindows()

mouse = mouseTest()
mouse.run()

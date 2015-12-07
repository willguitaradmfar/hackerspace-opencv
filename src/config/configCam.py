import numpy as np

from src.config.config import Config

from src.hands.moviment import Moviment

from src.hands.identify import Identify

class ConfigCam(Config):
    def __init__(self, fileConfName="camio.conf"):
        Config.__init__(self, fileConfName)

    def configure(self):
        self.medianBlur = self.getInt('Moviment.medianBlur')
        Moviment.medianBlur = self.medianBlur

        self.kernelVertical = self.getInt('Moviment.kernelVertical')
        Moviment.kernelVertical = self.kernelVertical

        self.kernelHorizontal = self.getInt('Moviment.kernelHorizontal')
        Moviment.kernelHorizontal = self.kernelHorizontal

        self.dilationInterator = self.getInt('Moviment.dilationInterator')
        Moviment.dilationInterator = self.dilationInterator

        self.erodeInterator = self.getInt('Moviment.erodeInterator')
        Moviment.erodeInterator = self.erodeInterator

        self.deslocamentoMax = self.getInt('Identify.deslocamentoMax')
        Identify.deslocamentoMax = self.deslocamentoMax

        self.minArea = self.getInt('Moviment.minArea')
        Moviment.minArea = self.minArea

        self.maxArea = self.getInt('Moviment.maxArea')
        Moviment.maxArea = self.maxArea

        self.modFrames = self.getInt('Main.ModFrames')

        self.window = self.getInt('window')


    def gaussCallback(self, value):
        try:
            if value % 2 == 0:
                value -= 1
            if value <= 0:
                value = 1

            Moviment.medianBlur = value
            self.set('Moviment.medianBlur', value);
        except:
            return

    def verticalCallback(self, value):
        Moviment.kernelVertical = value
        self.set('Moviment.kernelVertical', value);
        return

    def horizontalCallback(self, value):
        Moviment.kernelHorizontal = value
        self.set('Moviment.kernelHorizontal', value);
        return

    def dilationCallback(self, value):
        Moviment.dilationInterator = value
        self.set('Moviment.dilationInterator', value);
        return

    def erodeCallback(self, value):
        Moviment.erodeInterator = value
        self.set('Moviment.erodeInterator', value);
        return

    def velocidadeCallback(self, value):
        Identify.deslocamentoMax = value
        self.set('Identify.deslocamentoMax', value);
        return

    def minAreaCallback(self, value):
        Moviment.minArea = value
        self.set('Moviment.minArea', value);
        return

    def maxAreaCallback(self, value):
        Moviment.maxArea = value
        self.set('Moviment.maxArea', value);
        return

    def modFramesCallback(self, value):
        self.modFrames = value
        self.set('Main.ModFrames', value);
        return

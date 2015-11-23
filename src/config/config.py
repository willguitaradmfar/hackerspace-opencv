import numpy as np
import ConfigParser

class Config:
    def __init__(self, fileConfName):
        self.fileConfName = fileConfName
        self.config = ConfigParser.RawConfigParser()
        self.config.read(self.fileConfName)

    def set(self, key, value):
        self.config.set('Geral', key, value)

    def get(self, key):
        return self.config.get('Geral', key)

    def getInt(self, key):
        return int(self.config.get('Geral', key))

    def save(self):
        print("Salvando arquivo de configuracao: %s" % self.fileConfName)
        cfgfile = open(self.fileConfName,'w')
        self.config.write(cfgfile)

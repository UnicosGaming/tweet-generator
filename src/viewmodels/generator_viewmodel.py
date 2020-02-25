import os

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal

class GeneratorViewModel(QtCore.QObject):
    onNextBackground = pyqtSignal(str)
    onNextLogo_1 = pyqtSignal(str)
    onNextLogo_2 = pyqtSignal(str)
    onNextLeague = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        
        self.backgrounds_path = os.path.join(os.getcwd(), "resources", "backgrounds")
        self.Logo_1_path = os.path.join(os.getcwd(), "resources", "logos")
        self.Logo_2_path = os.path.join(os.getcwd(), "resources", "logos")
        self.League_path = os.path.join(os.getcwd(), "resources", "leagues")

        self.background_index = 0
        self.Logo_1_index = 0
        self.Logo_2_index = 0
        self.League_index = 0
        
        self.background_images = self.load_backgrounds()
        self.Logo_1_images = self.load_logo_1()
        self.Logo_2_images = self.load_logo_2()
        self.leagues_images = self.load_leagues()
    



######################################################################################################

#############################          DEF LOADS               #######################################

######################################################################################################




    def load_backgrounds(self):
        paths = []
        for d, _, f in os.walk(self.backgrounds_path):
            for file in f:
                paths.append(os.path.join(d,file))

        return paths

    def load_logo_1(self):
        paths = []
        for d, _, f in os.walk(self.Logo_1_path):
            for file in f:
                paths.append(os.path.join(d,file))

        return paths

    def load_logo_2(self):
        paths = []
        for d, _, f in os.walk(self.Logo_2_path):
            for file in f:
                paths.append(os.path.join(d,file))

        return paths

    def load_leagues(self):
        paths = []
        for d, _, f in os.walk(self.League_path):
            for file in f:
                paths.append(os.path.join(d,file))

        return paths


######################################################################################################

#############################          NEXT PICTURES           #######################################

######################################################################################################


    def next_background(self):
        self.background_index += 1
        
        if self.background_index >= len(self.background_images):
            self.background_index = 0

        self.onNextBackground.emit(self.background_images[self.background_index])


    def next_logo_1(self):
        self.Logo_1_index += 1
        
        if self.Logo_1_index >= len(self.Logo_1_images):
            self.Logo_1_index = 0

        self.onNextLogo_1.emit(self.Logo_1_images[self.Logo_1_index])


    def next_logo_2(self):
        self.Logo_2_index += 1
        
        if self.Logo_2_index >= len(self.Logo_2_images):
            self.Logo_2_index = 0

        self.onNextLogo_2.emit(self.Logo_2_images[self.Logo_2_index])


    def next_league(self):
        self.League_index += 1
        
        if self.League_index >= len(self.leagues_images):
            self.League_index = 0

        self.onNextLeague.emit(self.leagues_images[self.League_index])
        



######################################################################################################
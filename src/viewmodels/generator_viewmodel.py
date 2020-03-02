import os

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal

class GeneratorViewModel(QtCore.QObject):
    onNextBackground = pyqtSignal(str)
    onNextLogo_local = pyqtSignal(str)
    onNextLogo_visitor = pyqtSignal(str)
    onNextLeague = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        
        self.backgrounds_path = os.path.join(os.getcwd(), "resources", "backgrounds")
        self.Logo_local_path = os.path.join(os.getcwd(), "resources", "logos")
        self.Logo_visitor_path = os.path.join(os.getcwd(), "resources", "logos")
        self.League_path = os.path.join(os.getcwd(), "resources", "leagues")

        self.background_index = 0
        self.Logo_local_index = 0
        self.Logo_visitor_index = 0
        self.League_index = 0
        
        self.background_images = self.load_backgrounds()
        self.Logo_local_images = self.load_logo_local()
        self.Logo_visitor_images = self.load_logo_visitor()
        self.leagues_images = self.load_leagues()
    
    def load_backgrounds(self):
        paths = []
        for d, _, f in os.walk(self.backgrounds_path):
            for file in f:
                paths.append(os.path.join(d,file))
        return paths

    def load_logo_local(self):
        paths = []
        for d, _, f in os.walk(self.Logo_local_path):
            for file in f:
                paths.append(os.path.join(d,file))
        return paths

    def load_logo_visitor(self):
        paths = []
        for d, _, f in os.walk(self.Logo_visitor_path):
            for file in f:
                paths.append(os.path.join(d,file))
        return paths

    def load_leagues(self):
        paths = []
        for d, _, f in os.walk(self.League_path):
            for file in f:
                paths.append(os.path.join(d,file))
        return paths

    def next_background(self):
        self.background_index += 1        
        if self.background_index >= len(self.background_images):
            self.background_index = 0
        self.onNextBackground.emit(self.background_images[self.background_index])

    def next_logo_local(self):
        self.Logo_local_index += 1        
        if self.Logo_local_index >= len(self.Logo_local_images):
            self.Logo_local_index = 0
        self.onNextLogo_local.emit(self.Logo_local_images[self.Logo_local_index])


    def next_logo_visitor(self):
        self.Logo_visitor_index += 1        
        if self.Logo_visitor_index >= len(self.Logo_visitor_images):
            self.Logo_visitor_index = 0
        self.onNextLogo_visitor.emit(self.Logo_visitor_images[self.Logo_visitor_index])

    def next_league(self):
        self.League_index += 1        
        if self.League_index >= len(self.leagues_images):
            self.League_index = 0
        self.onNextLeague.emit(self.leagues_images[self.League_index])

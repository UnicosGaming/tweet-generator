import os

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal

class GeneratorViewModel(QtCore.QObject):
    onNexBackground = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        
        self.backgrounds_path = os.path.join(os.getcwd(), "resources", "backgrounds")

        self.background_index = 0
        self.background_images = self.load_backgrounds()
    
    def load_backgrounds(self):
        paths = []
        for d, _, f in os.walk(self.backgrounds_path):
            for file in f:
                paths.append(os.path.join(d,file))

        return paths

    def next_background(self):
        self.background_index += 1
        
        if self.background_index >= len(self.background_images):
            self.background_index = 0

        self.onNexBackground.emit(self.background_images[self.background_index])
        


from PyQt5 import QtWidgets

from src.views.generatorUI import Ui_MainWindow


# Replace with code generated from PyQt Designer
class GeneratorView(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, gui, viewmodel, parent=None):
        super().__init__(parent)

        self.viewmodel = viewmodel
        self.setupUi(self)

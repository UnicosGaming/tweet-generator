from PyQt5 import QtWidgets, QtGui

from src.views.generatorUI import Ui_MainWindow


# Replace with code generated from PyQt Designer
class GeneratorView(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, gui, viewmodel, parent=None):
        super().__init__(parent)

        print("hola")
        self.viewmodel = viewmodel
        self.setupUi(self)

        self.configure_signals()

    def configure_signals(self):
        # GUI signals
        self.btnNext.clicked.connect(self.viewmodel.next_background)

        # ViewModel signals
        self.viewmodel.onNexBackground.connect(self.show_background)
        
    def show_background(self, image_path):
        image = QtGui.QImage(image_path)
        pixmap = QtGui.QPixmap.fromImage(image)

        self.lbImage.setPixmap(pixmap.scaled(self.lbImage.size()))
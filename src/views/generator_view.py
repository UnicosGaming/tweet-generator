from PyQt5 import QtWidgets, QtGui

from src.views.generatorUI import Ui_MainWindow


# Replace with code generated from PyQt Designer
class GeneratorView(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, gui, viewmodel, parent=None):
        super().__init__(parent)

       
        self.viewmodel = viewmodel
        self.setupUi(self)

        self.configure_signals()





    def configure_signals(self):
        # GUI signals
            #Backgrounds 
        self.btnNext_Background.clicked.connect(self.viewmodel.next_background)
            #Logos
        self.btnNext_Logo.clicked.connect(self.viewmodel.next_logo_1)
        self.btnNext_Logo_2.clicked.connect(self.viewmodel.next_logo_2)
            #Leagues
        self.btnNext_League.clicked.connect(self.viewmodel.next_league)



        # ViewModel signals
            #Backgrounds             
        self.viewmodel.onNextBackground.connect(self.show_background)
            #Logos
        self.viewmodel.onNextLogo_1.connect(self.show_logo_1)
        self.viewmodel.onNextLogo_2.connect(self.show_logo_2)
            #Leagues
        self.viewmodel.onNextLeague.connect(self.show_leagues)
        


######################################################################################################

#############################         SHOW PICTURES            #######################################

######################################################################################################


    def show_background(self, image_path):
        image = QtGui.QImage(image_path)
        pixmap = QtGui.QPixmap.fromImage(image)

        self.lbl_background.setPixmap(pixmap.scaled(self.lbl_background.size()))



    def show_logo_1(self, image_path):
        image = QtGui.QImage(image_path)
        pixmap = QtGui.QPixmap.fromImage(image)

        self.lbl_logo_1.setPixmap(pixmap.scaled(self.lbl_logo_1.size()))



    def show_logo_2(self, image_path):
        image = QtGui.QImage(image_path)
        pixmap = QtGui.QPixmap.fromImage(image)

        self.lbl_logo_2.setPixmap(pixmap.scaled(self.lbl_logo_2.size()))



    def show_leagues(self, image_path):
        image = QtGui.QImage(image_path)
        pixmap = QtGui.QPixmap.fromImage(image)

        self.lbl_league.setPixmap(pixmap.scaled(self.lbl_league.size()))


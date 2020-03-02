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
        self.btnNext_Logo_local.clicked.connect(self.viewmodel.next_logo_local)
        self.btnNext_Logo_visitor.clicked.connect(self.viewmodel.next_logo_visitor)
            #Leagues
        self.btnNext_League.clicked.connect(self.viewmodel.next_league)
           




        # ViewModel signals
            #Backgrounds             
        self.viewmodel.onNextBackground.connect(self.show_background)
            #Logos
        self.viewmodel.onNextLogo_local.connect(self.show_logo_local)
        self.viewmodel.onNextLogo_visitor.connect(self.show_logo_visitor)
            #Leagues
        self.viewmodel.onNextLeague.connect(self.show_leagues)
            #TextBox
        self.txt_local.textChanged.connect(self.change_lbl_local)
        self.txt_visitor.textChanged.connect(self.change_lbl_visitor)
        self.txt_description.textChanged.connect(self.change_lbl_description)


######################################################################################################

#############################         CHANGE LABELS            #######################################

######################################################################################################


    def change_lbl_local(self):
        self.lbl_local.setText(self.txt_local.text())

    def change_lbl_visitor(self):
        self.lbl_visitor.setText(self.txt_visitor.text())

    def change_lbl_description(self):
        self.lbl_description.setText(self.txt_description.text())

        










######################################################################################################

#############################         SHOW PICTURES            #######################################

######################################################################################################


    def show_background(self, image_path):
        image = QtGui.QImage(image_path)
        pixmap = QtGui.QPixmap.fromImage(image)

        self.lbl_background.setPixmap(pixmap.scaled(self.lbl_background.size()))



    def show_logo_local(self, image_path):
        image = QtGui.QImage(image_path)
        pixmap = QtGui.QPixmap.fromImage(image)

        self.lbl_logo_local.setPixmap(pixmap.scaled(self.lbl_logo_local.size()))



    def show_logo_visitor(self, image_path):
        image = QtGui.QImage(image_path)
        pixmap = QtGui.QPixmap.fromImage(image)

        self.lbl_logo_visitor.setPixmap(pixmap.scaled(self.lbl_logo_visitor.size()))



    def show_leagues(self, image_path):
        image = QtGui.QImage(image_path)
        pixmap = QtGui.QPixmap.fromImage(image)

        self.lbl_league.setPixmap(pixmap.scaled(self.lbl_league.size()))


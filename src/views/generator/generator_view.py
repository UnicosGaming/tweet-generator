import os
from PyQt5 import QtWidgets, QtGui 

from src.views.generator.generatorUI import Ui_MainWindow
from src.viewmodels.configuration_viewmodel import ConfigurationViewModel
from src.views.configuration.configurationUI import Ui_Dialog as Configuration_UI
from src.views.configuration.configuration_view import ConfigurationView


# Replace with code generated from PyQt Designer
class GeneratorView(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, gui, viewmodel, parent=None):
        super().__init__(parent)
       
        self.viewmodel = viewmodel
        self.setupUi(self)
        self.set_icon()

        self.configure_signals()

    def set_icon(self):
        icon_path = os.path.join(os.getcwd(), "resources", "application", "256x256.png")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

    def configure_signals(self):
        # GUI signals
            #Backgrounds 
        self.btnNext_Background.clicked.connect(self.viewmodel.next_background)
            #Logos
        self.btnNext_Logo_local.clicked.connect(self.viewmodel.next_logo_local)
        self.btnNext_Logo_visitor.clicked.connect(self.viewmodel.next_logo_visitor)
            #Leagues
        self.btnNext_League.clicked.connect(self.viewmodel.next_league)
            #Configuration
        self.actionConfiguration.triggered.connect(self.open_configuration_dialog)

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
       
    def change_lbl_local(self):
        self.lbl_local.setText(self.txt_local.text())

    def change_lbl_visitor(self):
        self.lbl_visitor.setText(self.txt_visitor.text())

    def change_lbl_description(self):
        self.lbl_description.setText(self.txt_description.text())

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

    def open_configuration_dialog(self):
        configuration_vm = ConfigurationViewModel()
        configuration_gui = Configuration_UI()
        configuration_v = ConfigurationView(configuration_gui, viewmodel=configuration_vm)
        self.configuration_dialog = configuration_v 
        configuration_v.show()

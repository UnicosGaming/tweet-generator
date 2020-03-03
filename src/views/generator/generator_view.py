import os
from functools import partial
from PyQt5 import QtWidgets, QtGui 

from src.views.generator.generatorUI import Ui_MainWindow
from src.viewmodels.configuration_viewmodel import ConfigurationViewModel
from src.views.configuration.configurationUI import Ui_Dialog as Configuration_UI
from src.views.configuration.configuration_view import ConfigurationView
from src.services.configuration import ConfigurationService
from src.enums.Directions import Direction


# Replace with code generated from PyQt Designer
class GeneratorView(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, gui, viewmodel, parent=None):
        super().__init__(parent)
       
        self.viewmodel = viewmodel
        self.setupUi(self)
        self.configure_tab_controls()
        self.set_icon()

        self.configure_signals()

    '''
    Remove all control tabs except for the configured team
    '''
    def configure_tab_controls(self):
        tabKey = self.viewmodel.get_control_tab()
        tabs_to_remove = []
        for x in range(self.tbControls.count()):
            if not tabKey == self.tbControls.widget(x).objectName():
                tabs_to_remove.append(x)
        
        for x in tabs_to_remove:
            self.tbControls.removeTab(x)

    def set_icon(self):
        icon_path = os.path.join(os.getcwd(), "resources", "application", "256x256.png")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

    def configure_signals(self):
        # GUI signals
            #Backgrounds 
        self.btnNext_Background.clicked.connect(self.viewmodel.next_background)
            #Leagues
        self.btnNext_League.clicked.connect(self.viewmodel.next_league)
            #Configuration
        self.actionConfiguration.triggered.connect(self.open_configuration_dialog)
        
        # Tab Local - Visitor
        self.txtResultLocalLV.textChanged.connect(self.change_lbl_local)
        self.txtResultVisitorLV.textChanged.connect(self.change_lbl_visitor)
        self.txtMessageLV.textChanged.connect(self.change_lbl_description)
        self.btnNextLocalLV.clicked.connect(partial(self.viewmodel.change_logo_local, Direction.FORWARD))
        self.btnBackLocalLV.clicked.connect(partial(self.viewmodel.change_logo_local, Direction.BACKWARD))
        self.btnNextVisitorLV.clicked.connect(partial(self.viewmodel.change_logo_visitor, Direction.FORWARD))
        self.btnBackVisitorLV.clicked.connect(partial(self.viewmodel.change_logo_visitor, Direction.BACKWARD))

        # Tab A - B
        self.txtResultLocalAB.textChanged.connect(self.change_lbl_local)
        self.txtResultVisitorAB.textChanged.connect(self.change_lbl_visitor)
        self.txtMessageAB.textChanged.connect(self.change_lbl_description)
        self.btnNextLocalAB.clicked.connect(partial(self.viewmodel.change_logo_local, Direction.FORWARD))
        self.btnBackLocalAB.clicked.connect(partial(self.viewmodel.change_logo_local, Direction.BACKWARD))
        self.btnNextVisitorAB.clicked.connect(partial(self.viewmodel.change_logo_visitor, Direction.FORWARD))
        self.btnBackVisitorAB.clicked.connect(partial(self.viewmodel.change_logo_visitor, Direction.BACKWARD))

        # ViewModel signals
            #Backgrounds             
        self.viewmodel.onNextBackground.connect(self.show_background)
            #Logos
        self.viewmodel.onNextLogo_local.connect(self.show_logo_local)
        self.viewmodel.onNextLogo_visitor.connect(self.show_logo_visitor)
            #Leagues
        self.viewmodel.onNextLeague.connect(self.show_leagues)


    def change_lbl_local(self, value):
        self.lbl_local.setText(value)

    def change_lbl_visitor(self, value):
        self.lbl_visitor.setText(value)

    def change_lbl_description(self, value):
        self.lbl_description.setText(value)

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
        configuration_s = ConfigurationService()
        configuration_vm = ConfigurationViewModel(configuration_s)
        configuration_gui = Configuration_UI()
        configuration_v = ConfigurationView(configuration_gui, viewmodel=configuration_vm)
        self.configuration_dialog = configuration_v 
        configuration_v.show()

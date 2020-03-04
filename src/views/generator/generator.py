import os
from functools import partial
from PyQt5 import QtWidgets, QtGui 
from PyQt5 import QtCore

from src.views.generator.generatorUI import Ui_MainWindow
from src.views.configuration.configurationUI import Ui_Dialog as Configuration_UI
from src.views.configuration.configuration import ConfigurationView
from src.viewmodels.configuration import ConfigurationViewModel
from src.services.configuration import ConfigurationService
from src.services.event_channel import EventChannel
from src.enums.Directions import Direction


class GeneratorView(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, gui, viewmodel, parent=None):
        super().__init__(parent)
        # self.configuration_s = ConfigurationService()
        self.viewmodel = viewmodel
        self.setupUi(self)
        self.configure_signals()

        if self.is_configured():
            # Change the controls available for the configured team
            self.configure_tab_controls()
            # Establish the application window icon
            self.set_window_icon()
            
            # Initialize the application with some images
            self.initialize_screen()
        else:
            self.initialize_configuration()

    def configure_signals(self):
        # GUI signals
        self.btnChange_Background.clicked.connect(self.viewmodel.change_background)
        self.btnChange_Competition.clicked.connect(self.viewmodel.change_competition)
        self.actionConfiguration.triggered.connect(self.open_configuration_dialog)
        
        # Tab Local - Visitor
        self.txtResultLocalLV.textChanged.connect(self.change_result_team_a)
        self.txtResultVisitorLV.textChanged.connect(self.change_result_team_b)
        self.txtMessageLV.textChanged.connect(self.change_image_message)
        self.btnNextLocalLV.clicked.connect(partial(self.viewmodel.change_logo_team_a, Direction.FORWARD))
        self.btnBackLocalLV.clicked.connect(partial(self.viewmodel.change_logo_team_a, Direction.BACKWARD))
        self.btnNextVisitorLV.clicked.connect(partial(self.viewmodel.change_logo_team_b, Direction.FORWARD))
        self.btnBackVisitorLV.clicked.connect(partial(self.viewmodel.change_logo_team_b, Direction.BACKWARD))

        # Tab A - B
        self.txtResultLocalAB.textChanged.connect(self.change_result_team_a)
        self.txtResultVisitorAB.textChanged.connect(self.change_result_team_b)
        self.txtMessageAB.textChanged.connect(self.change_image_message)
        self.btnNextLocalAB.clicked.connect(partial(self.viewmodel.change_logo_team_a, Direction.FORWARD))
        self.btnBackLocalAB.clicked.connect(partial(self.viewmodel.change_logo_team_a, Direction.BACKWARD))
        self.btnNextVisitorAB.clicked.connect(partial(self.viewmodel.change_logo_team_b, Direction.FORWARD))
        self.btnBackVisitorAB.clicked.connect(partial(self.viewmodel.change_logo_team_b, Direction.BACKWARD))

        # ViewModel signals
        self.viewmodel.on_background_changed.connect(self.change_background)
        self.viewmodel.on_team_a_changed.connect(self.change_logo_team_a)
        self.viewmodel.on_team_b_changed.connect(self.change_logo_team_b)
        self.viewmodel.on_competition_changed.connect(self.change_logo_competition)
        
        # Services
        EventChannel().instance().subscribe("images_loaded", self.initialize_screen)


    def is_configured(self):
        return self.viewmodel.is_configured()

    def initialize_configuration(self):
        self.open_configuration_dialog()

    def initialize_screen(self):
        self.viewmodel.change_background()
        self.viewmodel.change_competition()
        self.viewmodel.change_logo_team_a(Direction.FORWARD)
        self.viewmodel.change_logo_team_b(Direction.FORWARD)

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

    '''
    Set the application icon on title bar
    '''
    def set_window_icon(self):
        icon_path = self.viewmodel.get_application_icon()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

    def change_result_team_a(self, value):
        self.lbl_local.setText(value)

    def change_result_team_b(self, value):
        self.lbl_visitor.setText(value)

    def change_image_message(self, value):
        self.lbl_description.setText(value)

    def change_background(self, image_path):
        image = QtGui.QImage(image_path)
        pixmap = QtGui.QPixmap.fromImage(image)

        self.lbl_background.setPixmap(pixmap.scaled(self.lbl_background.size()))

    def change_logo_team_a(self, image_path):
        image = QtGui.QImage(image_path)
        pixmap = QtGui.QPixmap.fromImage(image)

        self.lbl_logo_team_a.setPixmap(pixmap.scaled(self.lbl_logo_team_a.size()))

    def change_logo_team_b(self, image_path):
        image = QtGui.QImage(image_path)
        pixmap = QtGui.QPixmap.fromImage(image)

        self.lbl_logo_team_b.setPixmap(pixmap.scaled(self.lbl_logo_team_b.size()))

    def change_logo_competition(self, image_path):
        image = QtGui.QImage(image_path)
        pixmap = QtGui.QPixmap.fromImage(image)

        self.lbl_league.setPixmap(pixmap.scaled(self.lbl_league.size()))

    def open_configuration_dialog(self):
        configuration_vm = ConfigurationViewModel()
        configuration_gui = Configuration_UI()
        configuration_v = ConfigurationView(configuration_gui, viewmodel=configuration_vm)
        self.configuration_dialog = configuration_v 
        configuration_v.show()

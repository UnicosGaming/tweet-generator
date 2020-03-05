import os
from pathlib import Path
from functools import partial

from PyQt5 import QtWidgets, QtGui 
from PyQt5 import QtCore

from src.views.generator.generatorUI import Ui_MainWindow
from src.views.configuration.configurationUI import Ui_Dialog as Configuration_UI
from src.views.configuration.configuration import ConfigurationView
from src.viewmodels.configuration import ConfigurationViewModel
from src.services.configuration import ConfigurationService
from src.services.event_channel import EventChannel
from src.services.dialog import DialogService
from src.enums.Directions import Direction


class GeneratorView(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, gui, viewmodel, parent=None):
        super().__init__(parent)
        # self.configuration_s = ConfigurationService()
        self.viewmodel = viewmodel
        self.setupUi(self)
        self.configure_signals()

        if self.is_configured():
            # Change the inputs and panel tab available for the configured team
            self.configure_inputs_tab()
            self.configure_panel_tab()
            # Establish the application window icon
            self.set_window_icon()
            self.set_window_title()
            
            # Initialize the application with some images
            self.initialize_screen()
        else:
            self.initialize_configuration()

    def configure_signals(self):
        # GUI signals
        self.btnChange_Background.clicked.connect(self.viewmodel.change_background)
        self.btnChange_Competition.clicked.connect(self.viewmodel.change_competition)
        self.actionConfiguration.triggered.connect(self.open_configuration_dialog)
        self.action_UpdateImageLibrary.triggered.connect(lambda: EventChannel().instance().publish("image_path_changed"))
        
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
        EventChannel().instance().subscribe("backgrounds_loaded", self.viewmodel.change_background)
        EventChannel().instance().subscribe("logo_teams_loaded", self.__initialize_logo_teams)
        EventChannel().instance().subscribe("logo_competitions_loaded", self.viewmodel.change_competition)



    def is_configured(self):
        return self.viewmodel.is_configured()

    def initialize_configuration(self):
        self.open_configuration_dialog()

    '''
    Initialize the window with all available images
    '''
    def initialize_screen(self):
        self.viewmodel.change_background()
        self.viewmodel.change_competition()
        self.viewmodel.change_logo_team_a(Direction.FORWARD)
        self.viewmodel.change_logo_team_b(Direction.FORWARD)

    '''
    Show the logo images. Usually after reloading the image list
    '''
    def __initialize_logo_teams(self):
        self.viewmodel.change_logo_team_a(Direction.FORWARD)
        self.viewmodel.change_logo_team_b(Direction.FORWARD)

    '''
    Remove all input tabs except for the configured team
    '''
    def configure_inputs_tab(self):
        tabKey = self.viewmodel.get_controls_tab("inputs")
        tabs_to_remove = []
        for x in range(self.tbControls.count()):
            if not tabKey == self.tbControls.widget(x).objectName():
                tabs_to_remove.append(x)
        
        for x in tabs_to_remove:
            self.tbControls.removeTab(x)

    '''
    Remove all panels except for the configured team
    '''
    def configure_panel_tab(self):
        tabKey = self.viewmodel.get_controls_tab("panel")
        tabs_to_remove = []
        for x in range(self.tbPanel.count()):
            print(self.tbPanel.widget(x).objectName())
            if not tabKey == self.tbPanel.widget(x).objectName():
                tabs_to_remove.append(x)
        
        for x in tabs_to_remove:
            self.tbPanel.removeTab(x)

    '''
    Set the application icon on title bar
    '''
    def set_window_icon(self):
        icon_path = self.viewmodel.get_application_icon()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

    '''
    Add the team to the window title 
    '''
    def set_window_title(self):
        title = f"{self.windowTitle()} :: {ConfigurationService().instance().get_value('team')}"
        self.setWindowTitle(title)

    def change_result_team_a(self, value):
        self.lbl_local.setText(value)

    def change_result_team_b(self, value):
        self.lbl_visitor.setText(value)

    def change_image_message(self, value):
        self.lbl_description.setText(value)

    def change_background(self, image_path):
        image = self.__try_get_image(image_path)

        if image is None:
            EventChannel().instance().publish("background_reload")
        else:
            self.lbl_background.setPixmap(image.scaled(self.lbl_background.size()))

    def change_logo_team_a(self, image_path):
        image = self.__try_get_image(image_path)

        if image is None:
            EventChannel().instance().publish("logo_teams_reload")
        else:
            self.lbl_logo_team_a.setPixmap(image.scaled(self.lbl_logo_team_a.size()))

    def change_logo_team_b(self, image_path):
        image = self.__try_get_image(image_path)

        if image is None:
            EventChannel().instance().publish("logo_teams_reload")
        else:
            self.lbl_logo_team_b.setPixmap(image.scaled(self.lbl_logo_team_b.size()))
    
    def change_logo_competition(self, image_path):
        image = self.__try_get_image(image_path)

        if image is None:
            EventChannel().instance().publish("logo_competitions_reload")
        else:
            self.lbl_league.setPixmap(image.scaled(self.lbl_league.size()))

    '''
    Return the pixmap image if available
    '''
    def __try_get_image(self, image_path):
        # Check if the image still existing
        if os.path.exists(image_path):
            image = QtGui.QImage(image_path)
            pixmap = QtGui.QPixmap.fromImage(image)
            
            return pixmap
        
        path = Path(image_path)
        if path.parent.exists:
            # If the path does not contains images, notify to the user
            if not any([True for _ in os.scandir(path.parent)]):
                DialogService().instance().show_ok("Imágen no encontrada", "No se encuentra ninguna imágen. Abre la configuración y selecciona la ruta con las imágenes de la aplicación.")

        return None

    def open_configuration_dialog(self):
        configuration_vm = ConfigurationViewModel()
        configuration_gui = Configuration_UI()
        configuration_v = ConfigurationView(configuration_gui, viewmodel=configuration_vm)
        self.configuration_dialog = configuration_v 
        configuration_v.show()

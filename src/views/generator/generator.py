import os
import sys
from pathlib import Path
from functools import partial

from PyQt5 import QtWidgets, QtGui 
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from src.views.generator.generatorUI import Ui_MainWindow
from src.views.configuration.configurationUI import Ui_Dialog as Configuration_UI
from src.views.configuration.configuration import ConfigurationView
from src.viewmodels.configuration import ConfigurationViewModel
from src.services.configuration import ConfigurationService
from src.services.event_channel import EventChannel
from src.services.dialog import DialogService
from src.enums.Directions import Direction

class GeneratorViewBase(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, gui, viewmodel, parent):
        super().__init__(parent)

        # Event subscriptions
        EventChannel().instance().subscribe("configuration_team_changed", self.__ask_for_restart)

        self.viewmodel = viewmodel
        self.setupUi(self)

        # Change the inputs and panel tab available for the configured team
        self.configure_inputs_tab()
        self.configure_panel_tab()
        # Establish the application window icon
        self.set_window_icon()
        self.set_window_title()

    def configure_signals(self):
        # GUI signals
        self.btnChange_Background.clicked.connect(self.viewmodel.change_background)
        self.btn_save_image_r.clicked.connect(self.__save_image)
        self.btnChange_Competition.clicked.connect(self.viewmodel.change_competition)
        self.actionConfiguration.triggered.connect(self.open_configuration_dialog)
        self.action_UpdateImageLibrary.triggered.connect(lambda: EventChannel().instance().publish("image_path_changed"))

        # ViewModel signals
        self.viewmodel.on_background_changed.connect(self.change_background)
        self.viewmodel.on_team_a_changed.connect(self.change_logo_team_a)
        self.viewmodel.on_team_b_changed.connect(self.change_logo_team_b)
        self.viewmodel.on_competition_changed.connect(self.change_logo_competition)
        
        # Services
        EventChannel().instance().subscribe("backgrounds_loaded", self.viewmodel.change_background)
        EventChannel().instance().subscribe("logo_teams_loaded", self.__initialize_logo_teams)
        EventChannel().instance().subscribe("logo_competitions_loaded", self.viewmodel.change_competition)

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
            if tabKey == self.tbControls.widget(x).objectName():
                continue
            
            tabs_to_remove.append(x)
        
        # Remove the tabs by index, so we need to start by the higher value
        for x in sorted(tabs_to_remove, reverse=True):
            self.tbControls.removeTab(x)

    '''
    Remove all panels except for the configura ed team
    '''
    def configure_panel_tab(self):
        tabKey = self.viewmodel.get_controls_tab("panel")
        tabs_to_remove = []
        for x in range(self.tbPanel.count()):
            if tabKey == self.tbPanel.widget(x).objectName():
                continue
            
            tabs_to_remove.append(x)
        
        for x in sorted(tabs_to_remove, reverse=True):
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
        image = self.try_get_image(image_path)

        if image is None:
            EventChannel().instance().publish("background_reload")
        else:
            self.lbl_background.setPixmap(image.scaled(self.lbl_background.size()))

    def change_logo_team_a(self, image_path):
        image = self.try_get_image(image_path)

        if image is None:
            EventChannel().instance().publish("logo_teams_reload")
        else:
            self.lbl_logo_team_a.setPixmap(image.scaled(self.lbl_logo_team_a.size()))

    def change_logo_team_b(self, image_path):
        image = self.try_get_image(image_path)

        if image is None:
            EventChannel().instance().publish("logo_teams_reload")
        else:
            self.lbl_logo_team_b.setPixmap(image.scaled(self.lbl_logo_team_b.size()))
    
    def change_logo_competition(self, image_path):
        image = self.try_get_image(image_path)

        if image is None:
            EventChannel().instance().publish("logo_competitions_reload")
        else:
            self.lbl_competition.setPixmap(image.scaled(self.lbl_competition.size()))

    '''
    Return the pixmap image if available
    '''
    def try_get_image(self, image_path):
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

    '''
    Show a dialog asking for restart the application
    '''
    def __ask_for_restart(self):
        response = DialogService().instance().show_ok_cancel("Reiniciar aplicación", "Los cambios se aplicarán después de reiniciar la aplicación. ¿Desea reiniciar ahora?")
        if response:
            python = sys.executable
            os.execl(python, python, * sys.argv)

    '''
    Capture and save the image
    '''
    def __save_image(self):
        image_position = self.tbPanel.mapToGlobal(self.lbl_background.pos())
        width = self.lbl_background.geometry().width()
        height = self.lbl_background.geometry().height()

        screen = QApplication.primaryScreen()
        capture = screen.grabWindow(QApplication.desktop().winId(), image_position.x() + 2, image_position.y() + 2, width, height)

        file_name = DialogService().instance().show_save_file(self, "Nombre de la imágen")

        if file_name:
            capture.save(file_name)
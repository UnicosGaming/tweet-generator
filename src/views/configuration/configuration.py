import os
import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import pyqtSignal

from src.views.configuration.configurationUI import Ui_Dialog
from src.services.event_channel import EventChannel
from src.services.dialog import DialogService

class ConfigurationView(QtWidgets.QMainWindow, Ui_Dialog):
    on_configuration_changed = pyqtSignal()

    def __init__(self, gui, viewmodel, parent=None):
        super().__init__(parent)
        
        self.viewmodel = viewmodel
        self.setupUi(self)
        self.set_icon()
        self.configure_signals()

        self.load_teams()
        self.load_configuration()

    '''
    Configure the icon on title bar
    '''
    def set_icon(self):
        icon_path = self.viewmodel.get_application_icon()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

    def configure_signals(self):
        self.btnFolderDialog.clicked.connect(self.open_folder_dialog)

    def open_folder_dialog(self):
        folder_name = DialogService().instance().show_open_folder(self, "Selecciona el directorio")

        if folder_name:
            self.txtImagesFolderPath.setText(folder_name)

    '''
    Re-implement the closeEvent handler from Dialog in order to catch such event
    '''
    def closeEvent(self, event):
        is_team_changed = False
        is_image_path_changed = False

        team = self.get_selected_team()
        images_path = self.get_images_path()

        if team == None:
            DialogService().instance().show_information(self, "Selecciona el equipo", "Debes seleccionar un equipo de la lista")

            event.ignore()
            return

        if images_path == None:
            DialogService().instance().show_information(self, "Selecciona la ruta de las imágenes", "Debes seleccionar la ruta válida donde se guardan las imágenes y logos")
            
            event.ignore()
            return

        # If the team has changed, we need to ask for restart the application
        # in order to change the controls tab
        if team != self.viewmodel.get_team():
            is_team_changed = True
        
        if images_path != self.viewmodel.get_images_path():
            is_image_path_changed = True

        if team and images_path:
            self.viewmodel.set_team(team)
            self.viewmodel.set_images_path(images_path)
            self.viewmodel.save()
            self.viewmodel.load_configuration()

        if is_team_changed:
            EventChannel().instance().publish("configuration_team_changed")

        if is_image_path_changed:
            EventChannel().instance().publish("configuration_image_path_changed")

    '''
    Returns the selected team from the listView
    '''
    def get_selected_team(self): 
        selected_team = self.lstTeams.selectedItems()
        team = None

        if len(selected_team) > 0:
            team = selected_team[0].text()  

        return team
    
    '''
    Returns the images path if is a valid path
    '''
    def get_images_path(self):
        images_path = self.txtImagesFolderPath.text()

        if os.path.isdir(images_path):
            return images_path
        
        return None

    '''
    Load the teams available on teams.json into the listView
    '''
    def load_teams(self):
        teams = self.viewmodel.get_teams()
        self.lstTeams.addItems(teams)

    def load_configuration(self):
        if self.viewmodel.is_configured():
            # Select the row with the specific team
            items = self.lstTeams.findItems(self.viewmodel.get_team(),QtCore.Qt.MatchExactly)
            if len(items) > 0:
                item_model = self.lstTeams.indexFromItem(items[0])
                self.lstTeams.setCurrentRow(item_model.row())

            self.txtImagesFolderPath.setText(self.viewmodel.get_images_path())

    
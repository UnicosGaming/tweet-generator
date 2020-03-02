import os
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog

from src.views.configuration.configurationUI import Ui_Dialog

class ConfigurationView(QtWidgets.QMainWindow, Ui_Dialog):
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
        icon_path = os.path.join(os.getcwd(), "resources", "application", "256x256.png")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

    def configure_signals(self):
        self.btnFolderDialog.clicked.connect(self.open_folder_dialog)

    def open_folder_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly | QFileDialog.DontUseNativeDialog | QFileDialog.DontResolveSymlinks

        foldername = QFileDialog.getExistingDirectory(self, "Selecciona el directorio", options=options)

        if foldername:
            self.txtImagesFolderPath.setText(foldername)

    '''
    Re-implement the closeEvent handler from Dialog in order to catch such event
    '''
    def closeEvent(self, event):
        team = self.get_selected_team()
        images_path = self.get_images_path()

        if team == None:
            close = QtWidgets.QMessageBox.information(self, 
            "Selecciona el equipo", "Debes seleccionar un equipo de la lista",
            QtWidgets.QMessageBox.Close)

            event.ignore()
            return

        if images_path == None:
            close = QtWidgets.QMessageBox.information(self,
            "Selecciona la ruta de las imágenes",
            "Debes seleccionar la ruta válida donde se guardan las imágenes y logos",
            QtWidgets.QMessageBox.Close)

            event.ignore()
            return

        if team and images_path:
            self.viewmodel.set_value("team", team)
            self.viewmodel.set_value("images", images_path)
            self.viewmodel.set_value("configured", True)
            self.viewmodel.save()

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
        if self.viewmodel.get_value("configured"):
            # Select the row with the specific team
            items = self.lstTeams.findItems(self.viewmodel.get_value("team"),QtCore.Qt.MatchExactly)
            if len(items) > 0:
                item_model = self.lstTeams.indexFromItem(items[0])
                self.lstTeams.setCurrentRow(item_model.row())

            self.txtImagesFolderPath.setText(self.viewmodel.get_value("images"))

    
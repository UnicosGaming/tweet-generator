import os

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal

from src.services.configuration import ConfigurationService
from src.services.event_channel import EventChannel

from src.viewmodels.base import BaseViewModel

class GeneratorViewModel(QtCore.QObject, BaseViewModel):
    on_background_changed = pyqtSignal(str)
    on_team_a_changed = pyqtSignal(str)
    on_team_b_changed = pyqtSignal(str)
    on_competition_changed = pyqtSignal(str)
    on_configuration_changed = pyqtSignal()

    def __init__(self):
        super().__init__()
        
        EventChannel().instance().subscribe("image_path_changed", self.__load_images)

        self.__background_index = 0
        self.__logo_team_a_index = 0
        self.__logo_team_b_index = 0
        self.__logo_competition_index = 0
        
        self.__load_images()

    def __load_images(self):
        self.__background_images = self.__load_backgrounds()
        self.__logo_teams_images = self.__load_logos()
        self.__competition_images = self.__load_competitions()
        
        EventChannel().instance().publish("images_loaded")

    def __load_backgrounds(self):
        backgrounds_path = os.path.join(ConfigurationService().instance().get_value("images"), "backgrounds")
        paths = []

        for d, _, f in os.walk(backgrounds_path):
            for file in f:
                paths.append(os.path.join(d,file))
        
        return paths

    def __load_logos(self):
        logo_teams_path = os.path.join(ConfigurationService().instance().get_value("images"), "teams")
        paths = []

        for d, _, f in os.walk(logo_teams_path):
            for file in f:
                paths.append(os.path.join(d,file))
        
        return paths

    def __load_competitions(self):
        logo_competition_path = os.path.join(ConfigurationService().instance().get_value("images"), "competitions")
        paths = []

        for d, _, f in os.walk(logo_competition_path):
            for file in f:
                paths.append(os.path.join(d,file))
        
        return paths

    def change_background(self):
        if len(self.__background_images) == 0: return

        self.__background_index += 1        
        
        if self.__background_index >= len(self.__background_images):
            self.__background_index = 0
        
        self.on_background_changed.emit(self.__background_images[self.__background_index])

    def change_logo_team_a(self, direction):
        if len(self.__logo_teams_images) == 0: return

        self.__logo_team_a_index += direction.value

        if self.__logo_team_a_index >= len(self.__logo_teams_images):
            self.__logo_team_a_index = 0
        if self.__logo_team_a_index < 0:
            self.__logo_team_a_index = len(self.__logo_teams_images) - 1

        self.on_team_a_changed.emit(self.__logo_teams_images[self.__logo_team_a_index])

    def change_logo_team_b(self, direction):
        if len(self.__logo_teams_images) == 0: return

        self.__logo_team_b_index += direction.value

        if self.__logo_team_b_index >= len(self.__logo_teams_images):
            self.__logo_team_b_index = 0
        if self.__logo_team_b_index < 0:
            self.__logo_team_b_index = len(self.__logo_teams_images) - 1

        self.on_team_b_changed.emit(self.__logo_teams_images[self.__logo_team_b_index])

    def change_competition(self):
        if len(self.__competition_images) == 0: return

        self.__logo_competition_index += 1

        if self.__logo_competition_index >= len(self.__competition_images):
            self.__logo_competition_index = 0
        
        self.on_competition_changed.emit(self.__competition_images[self.__logo_competition_index])

    '''
    Return the tab key for the configured team
    '''
    def get_control_tab(self):
        team = ConfigurationService().instance().get_value("team")
        controls = ConfigurationService().instance().get_value("controls")

        return controls[team]
    
    def is_configured(self):
        return ConfigurationService().instance().get_value("configured")
    
    def get_application_icon(self):
        icon_name =  ConfigurationService().instance().get_application_value("icon")
    
        return os.path.join(os.getcwd(), "resources", "images", icon_name)
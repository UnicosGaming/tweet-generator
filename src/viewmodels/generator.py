import os

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal

from src.services.configuration import ConfigurationService
from src.services.event_channel import EventChannel

from src.viewmodels.base import ViewModelBase

class GeneratorViewModel(QtCore.QObject, ViewModelBase):
    on_background_changed = pyqtSignal(str)
    on_team_a_changed = pyqtSignal(str)
    on_team_b_changed = pyqtSignal(str)
    on_competition_changed = pyqtSignal(str)
    on_configuration_changed = pyqtSignal()

    def __init__(self):
        super().__init__()
        
        EventChannel().instance().subscribe("configuration_image_path_changed", self.__load_images)
        EventChannel().instance().subscribe("background_reload", self.__load_backgrounds_images)
        EventChannel().instance().subscribe("logo_teams_reload", self.__load_logo_teams_images)
        EventChannel().instance().subscribe("logo_competitions_reload", self.__load_logo_competitions_images)

        self.__background_index = 0
        self.__logo_team_a_index = 0
        self.__logo_team_b_index = 0
        self.__logo_competition_index = 0
        
        self.__load_images()

    def __load_images(self):
        self.__load_backgrounds_images()
        self.__load_logo_teams_images()
        self.__load_logo_competitions_images()

    def __load_backgrounds_images(self):
        self.__background_images = self.__load_backgrounds()
        
        EventChannel().instance().publish("backgrounds_loaded")

    def __load_logo_teams_images(self):
        self.__logo_teams_images = self.__load_logos()

        EventChannel().instance().publish("logo_teams_loaded")

    def __load_logo_competitions_images(self):
        self.__competition_images = self.__load_competitions()

        EventChannel().instance().publish("logo_competitions_loaded")

    '''
    Load the backgrounds image paths
    '''
    def __load_backgrounds(self):
        backgrounds_path = os.path.join(ConfigurationService().instance().get_value("images"), "backgrounds")
        paths = []

        for d, _, f in os.walk(backgrounds_path):
            for file in f:
                paths.append(os.path.join(d,file))
        
        return paths

    '''
    Load the logos paths
    '''
    def __load_logos(self):
        logo_teams_path = os.path.join(ConfigurationService().instance().get_value("images"), "teams")
        paths = []

        for d, _, f in os.walk(logo_teams_path):
            for file in f:
                paths.append(os.path.join(d,file))
        
        return paths

    '''
    Load the competition logo paths 
    '''
    def __load_competitions(self):
        logo_competition_path = os.path.join(ConfigurationService().instance().get_value("images"), "competitions")
        paths = []

        for d, _, f in os.walk(logo_competition_path):
            for file in f:
                paths.append(os.path.join(d,file))
        
        return paths

    '''
    Change the index over the background images and emit the new image path
    '''
    def change_background(self):
        if len(self.__background_images) == 0: return

        self.__background_index += 1        
        
        if self.__background_index >= len(self.__background_images):
            self.__background_index = 0
        
        self.on_background_changed.emit(self.__background_images[self.__background_index])

    '''
    Change the index over the logo team a images and emit the new image path
    '''
    def change_logo_team_a(self, direction):
        if len(self.__logo_teams_images) == 0: return

        self.__logo_team_a_index += direction.value

        if self.__logo_team_a_index >= len(self.__logo_teams_images):
            self.__logo_team_a_index = 0
        if self.__logo_team_a_index < 0:
            self.__logo_team_a_index = len(self.__logo_teams_images) - 1

        self.on_team_a_changed.emit(self.__logo_teams_images[self.__logo_team_a_index])

    '''
    Change the index over the logo team b images and emit the new image path
    '''
    def change_logo_team_b(self, direction):
        if len(self.__logo_teams_images) == 0: return

        self.__logo_team_b_index += direction.value

        if self.__logo_team_b_index >= len(self.__logo_teams_images):
            self.__logo_team_b_index = 0
        if self.__logo_team_b_index < 0:
            self.__logo_team_b_index = len(self.__logo_teams_images) - 1

        self.on_team_b_changed.emit(self.__logo_teams_images[self.__logo_team_b_index])
    
    '''
    Change the index over the competition images and emit the new image path
    '''
    def change_competition(self):
        if len(self.__competition_images) == 0: return

        self.__logo_competition_index += 1

        if self.__logo_competition_index >= len(self.__competition_images):
            self.__logo_competition_index = 0
        
        self.on_competition_changed.emit(self.__competition_images[self.__logo_competition_index])

    '''
    Return the tab key for the configured team
    '''
    def get_controls_tab(self, control):
        team = ConfigurationService().instance().get_value("team")
        controls = ConfigurationService().instance().get_value("controls")

        return controls[team][control]
        
    '''
    Check if the application is configured
    '''
    def is_configured(self):
        return ConfigurationService().instance().get_value("configured")
    
    def get_application_icon(self):
        icon_name =  ConfigurationService().instance().get_application_value("icon")
    
        return os.path.join(os.getcwd(), "resources", "images", icon_name)
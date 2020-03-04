import os

from src.services.configuration import ConfigurationService
from src.viewmodels.base import BaseViewModel

class ConfigurationViewModel(BaseViewModel):
    def __init__(self):
        super().__init__()

    def is_configured(self):
        return ConfigurationService().instance().get_value("configured")
    
    def get_team(self):
        return ConfigurationService().instance().get_value("team")

    def get_images_path(self):
        return ConfigurationService().instance().get_value("images")

    def set_team(self, value):
        ConfigurationService().instance().set_value("team", value)
    
    def set_images_path(self, value):
        ConfigurationService().instance().set_value("images", value)
    
    def get_teams(self):
        return ConfigurationService().instance().get_teams()

    def save(self):
        ConfigurationService().instance().set_value("configured", True)
        ConfigurationService().instance().save()

    def load_configuration(self):
        ConfigurationService().instance().load_configuration()
    

    

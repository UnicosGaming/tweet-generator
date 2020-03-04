import os

from src.viewmodels.base import BaseViewModel

class ConfigurationViewModel(BaseViewModel):
    def __init__(self, config_service):
        super().__init__(config_service)

    def is_configured(self):
        return self.config_service.get_value("configured")
    
    def get_team(self):
        return self.config_service.get_value("team")

    def get_images_path(self):
        return self.config_service.get_value("images")

    def set_team(self, value):
        self.config_service.set_value("team", value)
    
    def set_images_path(self, value):
        self.config_service.set_value("images", value)
    
    def get_teams(self):
        return self.config_service.get_teams()

    def save(self):
        self.config_service.set_value("configured", True)
        self.config_service.save()

    

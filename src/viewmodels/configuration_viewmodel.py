import os
import json

class ConfigurationViewModel():
    def __init__(self, config_service):
        self.__config_service = config_service

    def is_configured(self):
        return self.__config_service.get_value("configured")
    
    def get_team(self):
        return self.__config_service.get_value("team")

    def get_images_path(self):
        return self.__config_service.get_value("images")

    def set_team(self, value):
        self.__config_service.set_value("team", value)
    
    def set_images_path(self, value):
        self.__config_service.set_value("images", value)
    
    def get_teams(self):
        return self.__config_service.get_teams()

    def save(self):
        self.__config_service.set_value("configured", True)
        self.__config_service.save()

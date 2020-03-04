import os
import json

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal

class ConfigurationService():
    __instance = None

    def __init__(self):
        self.__config_path = os.path.join(os.getcwd(), "configuration.json")
        self.__teams_path = os.path.join(os.getcwd(), "teams.json")
        self.__configuration = None

        self.load_configuration()

    def instance(self):
        if ConfigurationService.__instance is None:
            ConfigurationService.__instance = ConfigurationService()

        return ConfigurationService.__instance

    '''
    Load the configuration from json file
    '''
    def load_configuration(self):
        with open(self.__config_path) as f:
            self.__configuration =  json.load(f)
    
    '''
    Save the configuration data into the configuration.json file
    '''
    def save(self):
        with open(self.__config_path, 'w', encoding='utf-8') as f:
            json.dump(self.__configuration, f, ensure_ascii=False, indent=4)

    '''
    Returns the value for the specific key
    '''
    def get_value(self, key):
        return self.__configuration[key]

    '''
    Return the value from the application section in the configuration file
    '''
    def get_application_value(self, key):
        return self.__configuration["application"][key]

    '''
    Change the configuration value with the specific key
    '''
    def set_value(self, key, value):
        self.__configuration[key] = value

    '''
    Returns a list of teams from the teams.json file
    '''
    def get_teams(self):
        with open(self.__teams_path) as f:
            data = json.load(f)
            return data["teams"]
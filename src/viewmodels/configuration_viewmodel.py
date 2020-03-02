import os
import json

class ConfigurationViewModel():
    def __init__(self):
        self.__config_path = os.path.join(os.getcwd(), "configuration.json")
        self.__teams_path = os.path.join(os.getcwd(), "teams.json")
        self.__configuration = None

        self.__initialize()

    def __initialize(self):
        if not os.path.exists(self.__config_path):
            self.__create()
            
        self.load_configuration()

    '''
    Create an initial configuration with empty values
    '''
    def __create(self):
        data = '{"team":"", "images":"", "configured":false}'
        
        self.__configuration = json.loads(data)
        
        self.save()

    '''
    Load the configuration from json file
    '''
    def load_configuration(self):
        with open(self.__config_path) as f:
            self.__configuration = json.load(f)

    '''
    Save the configuration data into the configuration.json file
    '''
    def save(self):
        with open(self.__config_path, 'w', encoding='utf-8') as f:
            json.dump(self.__configuration, f, ensure_ascii=False, indent=4)

    '''
    Change the configuration value with the specific key
    '''
    def set_value(self, key, value):
        self.__configuration[key] = value

    '''
    Returns the value for the specific key
    '''
    def get_value(self, key):
        return self.__configuration[key]

    '''
    Returns a list of teams from the teams.json file
    '''
    def get_teams(self):
        with open(self.__teams_path) as f:
            data = json.load(f)
            return data["teams"]
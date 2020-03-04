import os

class BaseViewModel():
    def __init__(self, config_service):
        self.config_service = config_service

    def get_application_icon(self):
        icon_name =  self.config_service.get_application_value("icon")
    
        return os.path.join(os.getcwd(), "resources", "images", icon_name)
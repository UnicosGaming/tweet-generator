import os

from src.services.configuration import ConfigurationService

class ViewModelBase():
    def get_application_icon(self):
        icon_name =  ConfigurationService().instance().get_application_value("icon")
    
        return os.path.join(os.getcwd(), "resources", "images", icon_name)
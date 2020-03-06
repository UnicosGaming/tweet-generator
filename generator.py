import sys
import os

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication

from src.views.generator.generatorUI import Ui_MainWindow
from src.views.generator.generator_LV import GeneratorViewLV
from src.viewmodels.generator import GeneratorViewModel

from src.views.configuration.configurationUI import Ui_Dialog as Configuration_UI
from src.views.configuration.configuration import ConfigurationView
from src.viewmodels.configuration import ConfigurationViewModel

from src.services.configuration import ConfigurationService
from src.services.event_channel import EventChannel
from src.services.factory_view_service import FactoryViewService

class Program():
    def __init__(self):
        pass
        EventChannel().instance().subscribe("configuration_team_changed", self.__initialize_view)
    '''
    Add the custom font to the resources
    '''
    def __initialize_font(self):
        font_name = ConfigurationService().instance().get_application_value("font")
        fonts_path = os.path.join(os.getcwd(), "resources", "fonts", font_name)
        QtGui.QFontDatabase.addApplicationFont(fonts_path)

    def __initialize_view(self):
        teamKey = ConfigurationService().instance().get_value("team")
        viewKey = ConfigurationService().instance().get_value("controls")[teamKey]["view"]

        self.view = FactoryViewService().instance().create_view(viewKey)
        self.view.show()

        EventChannel().instance().unsubscribe("configuration_team_changed", self.__initialize_view)

    def run(self):
        app = QApplication(sys.argv)

        # Configure font
        self.__initialize_font()

        if ConfigurationService().instance().get_value("configured"):
            self.__initialize_view()
        else:
            configuration_vm = ConfigurationViewModel()
            configuration_gui = Configuration_UI()
            configuration_v = ConfigurationView(configuration_gui, viewmodel=configuration_vm)
            self.configuration_dialog = configuration_v 
            configuration_v.show()


        sys.exit(app.exec())

if __name__ == '__main__':
    program = Program()
    program.run()
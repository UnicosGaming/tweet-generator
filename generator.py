import sys
import os

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication

from src.views.generator.generatorUI import Ui_MainWindow
from src.views.generator.generator import GeneratorView
from src.viewmodels.generator import GeneratorViewModel

from src.views.configuration.configurationUI import Ui_Dialog as Configuration_UI
from src.views.configuration.configuration import ConfigurationView
from src.viewmodels.configuration import ConfigurationViewModel

from src.services.configuration import ConfigurationService

def main():
    app = QApplication(sys.argv)
    fonts_path = os.path.join(os.getcwd(), "resources", "fonts", "UnicaOne-Regular.ttf")
    QtGui.QFontDatabase.addApplicationFont(fonts_path)

    # Initialize the configuration
    configuration_s = ConfigurationService()
    
    configuration_vm = ConfigurationViewModel(configuration_s)
    if not configuration_vm.is_configured():
        configuration_gui = Configuration_UI()
        configuration_v = ConfigurationView(configuration_gui, viewmodel=configuration_vm)
        configuration_v.show()

    viewmodel = GeneratorViewModel(configuration_s)

    gui = Ui_MainWindow()
    view = GeneratorView(gui, viewmodel = viewmodel)

    view.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
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

'''
Add the custom font to the resources
'''
def initialize_font():
    font_name = ConfigurationService().instance().get_application_value("font")
    fonts_path = os.path.join(os.getcwd(), "resources", "fonts", font_name)
    QtGui.QFontDatabase.addApplicationFont(fonts_path)

def main():
    app = QApplication(sys.argv)

    # Configure font
    initialize_font()

    viewmodel = GeneratorViewModel()

    gui = Ui_MainWindow()
    view = GeneratorView(gui, viewmodel = viewmodel)

    view.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
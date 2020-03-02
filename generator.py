import sys

from PyQt5.QtWidgets import QApplication

from src.views.generatorUI import Ui_MainWindow
from src.views.generator_view import GeneratorView
from src.views.configuration.configurationUI import Ui_Dialog as Configuration_UI
from src.views.configuration.configuration_view import ConfigurationView
from src.viewmodels.generator_viewmodel import GeneratorViewModel
from src.viewmodels.configuration_viewmodel import ConfigurationViewModel

def main():
    app = QApplication(sys.argv)

    # Initialize the configuration
    configuration_vm = ConfigurationViewModel()
    if not configuration_vm.get_value("configured"):
        configuration_gui = Configuration_UI()
        configuration_v = ConfigurationView(configuration_gui, viewmodel=configuration_vm)
        configuration_v.show()


    viewmodel = GeneratorViewModel()

    gui = Ui_MainWindow()
    view = GeneratorView(gui, viewmodel = viewmodel)

    view.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
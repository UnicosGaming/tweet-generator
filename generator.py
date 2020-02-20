import sys

from PyQt5.QtWidgets import QApplication

from src.views.generatorUI import Ui_MainWindow
from src.views.generator_view import GeneratorView
from src.viewmodels.generator_viewmodel import GeneratorViewModel

def main():
    app = QApplication(sys.argv)

    viewmodel = GeneratorViewModel()

    gui = Ui_MainWindow()
    view = GeneratorView(gui, viewmodel = viewmodel)

    view.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
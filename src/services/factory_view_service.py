from src.views.generator.generatorUI import Ui_MainWindow
from src.views.generator.generator_LV import GeneratorViewLV
from src.views.generator.generator_AB import GeneratorViewAB
from src.views.generator.generator_P import GeneratorViewP
from src.viewmodels.generator import GeneratorViewModel

class FactoryViewService():
    __instance = None

    def __init__(self):
        pass

    def instance(self):
        if FactoryViewService.__instance is None:
            FactoryViewService.__instance = FactoryViewService()
        
        return FactoryViewService.__instance

    def create_view(self, viewKey):
        if viewKey == "viewLV": return self.__create_view_LV()
        if viewKey == "viewAB": return self.__create_view_AB()
        if viewKey == "viewP": return self.__create_view_P()

    def __create_view_LV(self):
        viewmodel = GeneratorViewModel()
        gui = Ui_MainWindow()
        view = GeneratorViewLV(gui, viewmodel = viewmodel)

        return view

    def __create_view_AB(self):
        viewmodel = GeneratorViewModel()
        gui = Ui_MainWindow()
        view = GeneratorViewAB(gui, viewmodel = viewmodel)
        
        return view

    def __create_view_P(self):
        viewmodel = GeneratorViewModel()
        gui = Ui_MainWindow()
        view = GeneratorViewP(gui, viewmodel = viewmodel)
        
        return view
    
from PyQt5.QtWidgets import QApplication
from src.views.generator.generator import GeneratorViewBase
from src.services.dialog import DialogService

class GeneratorViewP(GeneratorViewBase):
    def __init__(self, gui, viewmodel, parent=None):
        super().__init__(gui, viewmodel, parent)

        self.configure_signals()
        self.initialize_screen()

    def configure_signals(self):
        super().configure_signals()

        # UI
        self.btn_change_background_p.clicked.connect(self.viewmodel.change_background)
        self.btn_save_image_p.clicked.connect(self.__save_image)
        self.txt_car.textChanged.connect(self.__change_car)
        self.txt_driver.textChanged.connect(self.__change_driver)
        self.txt_position.textChanged.connect(self.__change_position)
        self.txt_track.textChanged.connect(self.__change_track)

        # Viewmodels
        self.viewmodel.on_background_changed.connect(self.change_background)

    def __change_car(self, value):
        self.lbl_car.setText(value)
        
    def __change_driver(self, value):
        self.lbl_driver.setText(value)
        
    def __change_position(self, value):
        self.lbl_position.setText(value)
        
    def __change_track(self, value):
        self.lbl_track.setText(value)

    '''
    Capture and save the image
    '''
    def __save_image(self):
        image_position = self.tbPanel.mapToGlobal(self.lbl_background_panel_p.pos())
        width = self.lbl_background_panel_p.geometry().width()
        height = self.lbl_background_panel_p.geometry().height()

        screen = QApplication.primaryScreen()
        capture = screen.grabWindow(QApplication.desktop().winId(), image_position.x() + 2, image_position.y() + 2, width, height)

        file_name = DialogService().instance().show_save_file(self, "Nombre de la imágen")

        if file_name:
            capture.save(file_name)

    def change_background(self, image_path):
        image = self.try_get_image(image_path)

        if image is None:
            EventChannel().instance().publish("background_reload")
        else:
            self.lbl_background_panel_p.setPixmap(image.scaled(self.lbl_background.size()))
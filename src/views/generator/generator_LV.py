from functools import partial
from src.views.generator.generator import GeneratorViewBase
from src.enums.Directions import Direction

class GeneratorViewLV(GeneratorViewBase):
    def __init__(self, gui, viewmodel, parent=None):
        super().__init__(gui, viewmodel, parent)

        self.configure_signals()

        self.initialize_screen()

    def configure_signals(self):
        super().configure_signals()
        
        self.txtResultLocalLV.textChanged.connect(self.change_result_team_a)
        self.txtResultVisitorLV.textChanged.connect(self.change_result_team_b)
        self.txtMessageLV.textChanged.connect(self.change_image_message)
        self.btnNextLocalLV.clicked.connect(partial(self.viewmodel.change_logo_team_a, Direction.FORWARD))
        self.btnBackLocalLV.clicked.connect(partial(self.viewmodel.change_logo_team_a, Direction.BACKWARD))
        self.btnNextVisitorLV.clicked.connect(partial(self.viewmodel.change_logo_team_b, Direction.FORWARD))
        self.btnBackVisitorLV.clicked.connect(partial(self.viewmodel.change_logo_team_b, Direction.BACKWARD))
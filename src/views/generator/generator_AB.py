from functools import partial
from src.views.generator.generator import GeneratorViewBase
from src.enums.Directions import Direction

class GeneratorViewAB(GeneratorViewBase):
    def __init__(self, gui, viewmodel, parent=None):
        super().__init__(gui, viewmodel, parent)

        self.configure_signals()

        self.initialize_screen()

    def configure_signals(self):
        super().configure_signals()

        self.txtResultLocalAB.textChanged.connect(self.change_result_team_a)
        self.txtResultVisitorAB.textChanged.connect(self.change_result_team_b)
        self.txtMessageAB.textChanged.connect(self.change_image_message)
        self.btnNextLocalAB.clicked.connect(partial(self.viewmodel.change_logo_team_a, Direction.FORWARD))
        self.btnBackLocalAB.clicked.connect(partial(self.viewmodel.change_logo_team_a, Direction.BACKWARD))
        self.btnNextVisitorAB.clicked.connect(partial(self.viewmodel.change_logo_team_b, Direction.FORWARD))
        self.btnBackVisitorAB.clicked.connect(partial(self.viewmodel.change_logo_team_b, Direction.BACKWARD))

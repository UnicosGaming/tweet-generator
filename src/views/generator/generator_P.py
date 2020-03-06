from src.views.generator.generator import GeneratorViewBase

class GeneratorViewP(GeneratorViewBase):
    def __init__(self, gui, viewmodel, parent=None):
        super().__init__(gui, viewmodel, parent)

        self.configure_signals()

    def configure_signals(self):
        super().configure_signals()
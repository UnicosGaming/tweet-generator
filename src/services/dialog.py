from PyQt5.QtWidgets import QMessageBox

class DialogService():
    __instance = None

    def __init__(self):
        pass
    
    def instance(self):
        if DialogService.__instance is None:
            DialogService.__instance = DialogService()

        return DialogService.__instance

    '''
    Show a dialog with the OK button.
    Return True if OK, otherwise False
    '''
    def show_ok(self, title, message):
        dlg = QMessageBox()
        dlg.setWindowTitle(title)
        dlg.setText(message)
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.exec()
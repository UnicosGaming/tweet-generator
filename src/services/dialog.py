from PyQt5.QtWidgets import QMessageBox

class DialogService():
    __instance = None

    def __init__(self):
        pass
    
    def instance(self):
        if DialogService.__instance is None:
            DialogService.__instance = DialogService()

        return DialogService.__instance

    def show_ok(self, title, message):
        dlg = QMessageBox()
        dlg.setWindowTitle(title)
        dlg.setText(message)
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.exec()

    def show_ok_cancel(self, title, message):
        dlg = QMessageBox()
        dlg.setWindowTitle(title)
        dlg.setText(message)
        dlg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        if dlg.exec() == QMessageBox.Ok:
            return True
        
        return False
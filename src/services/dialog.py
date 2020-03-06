from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog

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

    def show_information(self, parent, title, message):
         QtWidgets.QMessageBox.information(parent, title, message, QtWidgets.QMessageBox.Close)

    def show_ok_cancel(self, title, message):
        dlg = QMessageBox()
        dlg.setWindowTitle(title)
        dlg.setText(message)
        dlg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        if dlg.exec() == QMessageBox.Ok:
            return True
        
        return False

    def show_open_folder(self, parent, title):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly | QFileDialog.DontUseNativeDialog | QFileDialog.DontResolveSymlinks

        folder_name = QFileDialog.getExistingDirectory(parent, title, options=options)

        return folder_name

    def show_save_file(self, parent, title):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        
        file_name, _ = QFileDialog.getSaveFileName(parent, title, "",  "Image files (*.jpg *.png)")

        return file_name
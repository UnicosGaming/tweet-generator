# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configuration.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(363, 189)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(363, 189))
        Dialog.setMaximumSize(QtCore.QSize(363, 189))
        self.lstTeams = QtWidgets.QListWidget(Dialog)
        self.lstTeams.setGeometry(QtCore.QRect(10, 40, 341, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lstTeams.setFont(font)
        self.lstTeams.setObjectName("lstTeams")
        self.txtImagesFolderPath = QtWidgets.QLineEdit(Dialog)
        self.txtImagesFolderPath.setGeometry(QtCore.QRect(10, 160, 261, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.txtImagesFolderPath.setFont(font)
        self.txtImagesFolderPath.setObjectName("txtImagesFolderPath")
        self.btnFolderDialog = QtWidgets.QPushButton(Dialog)
        self.btnFolderDialog.setGeometry(QtCore.QRect(280, 160, 75, 23))
        self.btnFolderDialog.setObjectName("btnFolderDialog")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "UG Clips :: Configuración"))
        self.txtImagesFolderPath.setPlaceholderText(_translate("Dialog", "Ruta del directorio de imágenes del equipo"))
        self.btnFolderDialog.setText(_translate("Dialog", "Seleccionar..."))
        self.label.setText(_translate("Dialog", "Selecciona tu equipo"))

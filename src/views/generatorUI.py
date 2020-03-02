# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\views\generator.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1053, 713)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnNext_Background = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext_Background.setGeometry(QtCore.QRect(170, 10, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnNext_Background.setFont(font)
        self.btnNext_Background.setObjectName("btnNext_Background")
        self.lbl_background = QtWidgets.QLabel(self.centralwidget)
        self.lbl_background.setGeometry(QtCore.QRect(10, 50, 1024, 512))
        self.lbl_background.setObjectName("lbl_background")
        self.lbl_logo_local = QtWidgets.QLabel(self.centralwidget)
        self.lbl_logo_local.setGeometry(QtCore.QRect(160, 230, 200, 200))
        self.lbl_logo_local.setObjectName("lbl_logo_local")
        self.lbl_logo_visitor = QtWidgets.QLabel(self.centralwidget)
        self.lbl_logo_visitor.setGeometry(QtCore.QRect(710, 230, 200, 200))
        self.lbl_logo_visitor.setObjectName("lbl_logo_visitor")
        self.lbl_league = QtWidgets.QLabel(self.centralwidget)
        self.lbl_league.setGeometry(QtCore.QRect(20, 60, 151, 101))
        self.lbl_league.setObjectName("lbl_league")
        self.lbl_vs = QtWidgets.QLabel(self.centralwidget)
        self.lbl_vs.setGeometry(QtCore.QRect(500, 290, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_vs.setFont(font)
        self.lbl_vs.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_vs.setObjectName("lbl_vs")
        self.lbl_local = QtWidgets.QLabel(self.centralwidget)
        self.lbl_local.setGeometry(QtCore.QRect(370, 270, 120, 100))
        font = QtGui.QFont()
        font.setPointSize(70)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_local.setFont(font)
        self.lbl_local.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_local.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_local.setObjectName("lbl_local")
        self.lbl_visitor = QtWidgets.QLabel(self.centralwidget)
        self.lbl_visitor.setGeometry(QtCore.QRect(580, 270, 120, 100))
        font = QtGui.QFont()
        font.setPointSize(70)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_visitor.setFont(font)
        self.lbl_visitor.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_visitor.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_visitor.setObjectName("lbl_visitor")
        self.lbl_description = QtWidgets.QLabel(self.centralwidget)
        self.lbl_description.setGeometry(QtCore.QRect(60, 430, 941, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_description.setFont(font)
        self.lbl_description.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_description.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_description.setObjectName("lbl_description")
        self.txt_local = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_local.setGeometry(QtCore.QRect(250, 600, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txt_local.setFont(font)
        self.txt_local.setMaxLength(2)
        self.txt_local.setObjectName("txt_local")
        self.txt_visitor = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_visitor.setGeometry(QtCore.QRect(570, 600, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txt_visitor.setFont(font)
        self.txt_visitor.setMaxLength(2)
        self.txt_visitor.setObjectName("txt_visitor")
        self.txt_description = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_description.setGeometry(QtCore.QRect(800, 600, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txt_description.setFont(font)
        self.txt_description.setMaxLength(250)
        self.txt_description.setObjectName("txt_description")
        self.btnNext_League = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext_League.setGeometry(QtCore.QRect(10, 10, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnNext_League.setFont(font)
        self.btnNext_League.setObjectName("btnNext_League")
        self.btnNext_Logo_local = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext_Logo_local.setGeometry(QtCore.QRect(140, 630, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnNext_Logo_local.setFont(font)
        self.btnNext_Logo_local.setObjectName("btnNext_Logo_local")
        self.btnNext_Logo_visitor = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext_Logo_visitor.setGeometry(QtCore.QRect(460, 630, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnNext_Logo_visitor.setFont(font)
        self.btnNext_Logo_visitor.setObjectName("btnNext_Logo_visitor")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 600, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 600, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(720, 600, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btnNext_League.raise_()
        self.btnNext_Logo_local.raise_()
        self.btnNext_Logo_visitor.raise_()
        self.lbl_background.raise_()
        self.btnNext_Background.raise_()
        self.lbl_logo_local.raise_()
        self.lbl_logo_visitor.raise_()
        self.lbl_league.raise_()
        self.lbl_vs.raise_()
        self.lbl_local.raise_()
        self.lbl_visitor.raise_()
        self.lbl_description.raise_()
        self.txt_local.raise_()
        self.txt_visitor.raise_()
        self.txt_description.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1053, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionConfiguration = QtWidgets.QAction(MainWindow)
        self.actionConfiguration.setObjectName("actionConfiguration")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionConfiguration)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UG Tweet Generator"))
        self.btnNext_Background.setText(_translate("MainWindow", "Cambiar fondo"))
        self.lbl_background.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_logo_local.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_logo_visitor.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_league.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_vs.setText(_translate("MainWindow", "VS"))
        self.lbl_local.setText(_translate("MainWindow", "0"))
        self.lbl_visitor.setText(_translate("MainWindow", "0"))
        self.lbl_description.setText(_translate("MainWindow", "X"))
        self.btnNext_League.setText(_translate("MainWindow", "Cambiar logo liga"))
        self.btnNext_Logo_local.setText(_translate("MainWindow", "Cambiar equipo local"))
        self.btnNext_Logo_visitor.setText(_translate("MainWindow", "Cambiar equipo visitante"))
        self.label.setText(_translate("MainWindow", "Resultado equipo local"))
        self.label_2.setText(_translate("MainWindow", "Resultado equipo visitante"))
        self.label_3.setText(_translate("MainWindow", "Descripción"))
        self.menuFile.setTitle(_translate("MainWindow", "Archivo"))
        self.actionConfiguration.setText(_translate("MainWindow", "Configuration"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

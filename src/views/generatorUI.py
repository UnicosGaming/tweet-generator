# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\generator.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnNext_Background = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext_Background.setGeometry(QtCore.QRect(10, 10, 111, 23))
        self.btnNext_Background.setObjectName("btnNext_Background")
        self.lbl_background = QtWidgets.QLabel(self.centralwidget)
        self.lbl_background.setGeometry(QtCore.QRect(10, 40, 1280, 720))
        self.lbl_background.setObjectName("lbl_background")
        self.btnNext_Logo = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext_Logo.setGeometry(QtCore.QRect(150, 10, 101, 23))
        self.btnNext_Logo.setObjectName("btnNext_Logo")
        self.btnNext_League = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext_League.setGeometry(QtCore.QRect(400, 10, 75, 23))
        self.btnNext_League.setObjectName("btnNext_League")
        self.lbl_logo_1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_logo_1.setGeometry(QtCore.QRect(310, 320, 181, 161))
        self.lbl_logo_1.setObjectName("lbl_logo_1")
        self.lbl_logo_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_logo_2.setGeometry(QtCore.QRect(890, 330, 181, 161))
        self.lbl_logo_2.setObjectName("lbl_logo_2")
        self.btnNext_Logo_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext_Logo_2.setGeometry(QtCore.QRect(260, 10, 111, 23))
        self.btnNext_Logo_2.setObjectName("btnNext_Logo_2")
        self.lbl_league = QtWidgets.QLabel(self.centralwidget)
        self.lbl_league.setGeometry(QtCore.QRect(50, 90, 151, 101))
        self.lbl_league.setObjectName("lbl_league")
        self.lbl_background.raise_()
        self.btnNext_Background.raise_()
        self.btnNext_Logo.raise_()
        self.btnNext_League.raise_()
        self.lbl_logo_1.raise_()
        self.lbl_logo_2.raise_()
        self.btnNext_Logo_2.raise_()
        self.lbl_league.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 21))
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
        self.btnNext_Background.setText(_translate("MainWindow", "Next background"))
        self.lbl_background.setText(_translate("MainWindow", "TextLabel"))
        self.btnNext_Logo.setText(_translate("MainWindow", "Next logo local"))
        self.btnNext_League.setText(_translate("MainWindow", "Next league"))
        self.lbl_logo_1.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_logo_2.setText(_translate("MainWindow", "TextLabel"))
        self.btnNext_Logo_2.setText(_translate("MainWindow", "Next logo visitante"))
        self.lbl_league.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionConfiguration.setText(_translate("MainWindow", "Configuration"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

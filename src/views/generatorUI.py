# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generator.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnNext = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.btnNext.setObjectName("btnNext")
        self.lbImage = QtWidgets.QLabel(self.centralwidget)
        self.lbImage.setGeometry(QtCore.QRect(10, 50, 611, 381))
        self.lbImage.setObjectName("lbImage")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
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
        self.btnNext.setText(_translate("MainWindow", "Next"))
        self.lbImage.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionConfiguration.setText(_translate("MainWindow", "Configuration"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

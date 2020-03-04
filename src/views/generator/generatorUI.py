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
        MainWindow.resize(1053, 713)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnChange_Background = QtWidgets.QPushButton(self.centralwidget)
        self.btnChange_Background.setGeometry(QtCore.QRect(170, 10, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnChange_Background.setFont(font)
        self.btnChange_Background.setObjectName("btnChange_Background")
        self.lbl_background = QtWidgets.QLabel(self.centralwidget)
        self.lbl_background.setGeometry(QtCore.QRect(10, 50, 1021, 512))
        self.lbl_background.setObjectName("lbl_background")
        self.lbl_logo_team_a = QtWidgets.QLabel(self.centralwidget)
        self.lbl_logo_team_a.setGeometry(QtCore.QRect(90, 230, 200, 200))
        self.lbl_logo_team_a.setObjectName("lbl_logo_team_a")
        self.lbl_logo_team_b = QtWidgets.QLabel(self.centralwidget)
        self.lbl_logo_team_b.setGeometry(QtCore.QRect(710, 230, 200, 200))
        self.lbl_logo_team_b.setObjectName("lbl_logo_team_b")
        self.lbl_league = QtWidgets.QLabel(self.centralwidget)
        self.lbl_league.setGeometry(QtCore.QRect(20, 60, 151, 101))
        self.lbl_league.setObjectName("lbl_league")
        self.lbl_vs = QtWidgets.QLabel(self.centralwidget)
        self.lbl_vs.setGeometry(QtCore.QRect(470, 290, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Unica One")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_vs.setFont(font)
        self.lbl_vs.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_vs.setObjectName("lbl_vs")
        self.lbl_local = QtWidgets.QLabel(self.centralwidget)
        self.lbl_local.setGeometry(QtCore.QRect(340, 270, 120, 100))
        font = QtGui.QFont()
        font.setFamily("Unica One")
        font.setPointSize(70)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_local.setFont(font)
        self.lbl_local.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_local.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_local.setObjectName("lbl_local")
        self.lbl_visitor = QtWidgets.QLabel(self.centralwidget)
        self.lbl_visitor.setGeometry(QtCore.QRect(550, 270, 120, 100))
        font = QtGui.QFont()
        font.setFamily("Unica One")
        font.setPointSize(70)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_visitor.setFont(font)
        self.lbl_visitor.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_visitor.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_visitor.setObjectName("lbl_visitor")
        self.lbl_description = QtWidgets.QLabel(self.centralwidget)
        self.lbl_description.setGeometry(QtCore.QRect(60, 430, 961, 100))
        font = QtGui.QFont()
        font.setFamily("Unica One")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_description.setFont(font)
        self.lbl_description.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_description.setText("")
        self.lbl_description.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_description.setObjectName("lbl_description")
        self.btnChange_Competition = QtWidgets.QPushButton(self.centralwidget)
        self.btnChange_Competition.setGeometry(QtCore.QRect(10, 10, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnChange_Competition.setFont(font)
        self.btnChange_Competition.setObjectName("btnChange_Competition")
        self.tbControls = QtWidgets.QTabWidget(self.centralwidget)
        self.tbControls.setGeometry(QtCore.QRect(10, 570, 1021, 101))
        self.tbControls.setAutoFillBackground(True)
        self.tbControls.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tbControls.setDocumentMode(False)
        self.tbControls.setTabBarAutoHide(True)
        self.tbControls.setObjectName("tbControls")
        self.tbLV = QtWidgets.QWidget()
        self.tbLV.setObjectName("tbLV")
        self.btnBackLocalLV = QtWidgets.QPushButton(self.tbLV)
        self.btnBackLocalLV.setGeometry(QtCore.QRect(100, 11, 31, 23))
        self.btnBackLocalLV.setObjectName("btnBackLocalLV")
        self.btnNextLocalLV = QtWidgets.QPushButton(self.tbLV)
        self.btnNextLocalLV.setGeometry(QtCore.QRect(210, 11, 31, 23))
        self.btnNextLocalLV.setObjectName("btnNextLocalLV")
        self.label = QtWidgets.QLabel(self.tbLV)
        self.label.setGeometry(QtCore.QRect(150, 13, 41, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tbLV)
        self.label_2.setGeometry(QtCore.QRect(760, 12, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btnBackVisitorLV = QtWidgets.QPushButton(self.tbLV)
        self.btnBackVisitorLV.setGeometry(QtCore.QRect(720, 10, 31, 23))
        self.btnBackVisitorLV.setObjectName("btnBackVisitorLV")
        self.btnNextVisitorLV = QtWidgets.QPushButton(self.tbLV)
        self.btnNextVisitorLV.setGeometry(QtCore.QRect(830, 10, 31, 23))
        self.btnNextVisitorLV.setObjectName("btnNextVisitorLV")
        self.label_3 = QtWidgets.QLabel(self.tbLV)
        self.label_3.setGeometry(QtCore.QRect(450, 12, 81, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtResultLocalLV = QtWidgets.QLineEdit(self.tbLV)
        self.txtResultLocalLV.setGeometry(QtCore.QRect(410, 11, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.txtResultLocalLV.setFont(font)
        self.txtResultLocalLV.setText("")
        self.txtResultLocalLV.setMaxLength(2)
        self.txtResultLocalLV.setAlignment(QtCore.Qt.AlignCenter)
        self.txtResultLocalLV.setObjectName("txtResultLocalLV")
        self.txtResultVisitorLV = QtWidgets.QLineEdit(self.tbLV)
        self.txtResultVisitorLV.setGeometry(QtCore.QRect(530, 10, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.txtResultVisitorLV.setFont(font)
        self.txtResultVisitorLV.setText("")
        self.txtResultVisitorLV.setMaxLength(2)
        self.txtResultVisitorLV.setAlignment(QtCore.Qt.AlignCenter)
        self.txtResultVisitorLV.setObjectName("txtResultVisitorLV")
        self.txtMessageLV = QtWidgets.QLineEdit(self.tbLV)
        self.txtMessageLV.setGeometry(QtCore.QRect(212, 50, 541, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.txtMessageLV.setFont(font)
        self.txtMessageLV.setText("")
        self.txtMessageLV.setMaxLength(150)
        self.txtMessageLV.setClearButtonEnabled(False)
        self.txtMessageLV.setObjectName("txtMessageLV")
        self.tbControls.addTab(self.tbLV, "")
        self.tbAB = QtWidgets.QWidget()
        self.tbAB.setObjectName("tbAB")
        self.btnBackVisitorAB = QtWidgets.QPushButton(self.tbAB)
        self.btnBackVisitorAB.setGeometry(QtCore.QRect(720, 10, 31, 23))
        self.btnBackVisitorAB.setObjectName("btnBackVisitorAB")
        self.label_4 = QtWidgets.QLabel(self.tbAB)
        self.label_4.setGeometry(QtCore.QRect(140, 12, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txtResultLocalAB = QtWidgets.QLineEdit(self.tbAB)
        self.txtResultLocalAB.setGeometry(QtCore.QRect(410, 11, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.txtResultLocalAB.setFont(font)
        self.txtResultLocalAB.setText("")
        self.txtResultLocalAB.setMaxLength(2)
        self.txtResultLocalAB.setAlignment(QtCore.Qt.AlignCenter)
        self.txtResultLocalAB.setObjectName("txtResultLocalAB")
        self.btnNextVisitorAB = QtWidgets.QPushButton(self.tbAB)
        self.btnNextVisitorAB.setGeometry(QtCore.QRect(830, 10, 31, 23))
        self.btnNextVisitorAB.setObjectName("btnNextVisitorAB")
        self.label_5 = QtWidgets.QLabel(self.tbAB)
        self.label_5.setGeometry(QtCore.QRect(450, 12, 81, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txtResultVisitorAB = QtWidgets.QLineEdit(self.tbAB)
        self.txtResultVisitorAB.setGeometry(QtCore.QRect(530, 10, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.txtResultVisitorAB.setFont(font)
        self.txtResultVisitorAB.setText("")
        self.txtResultVisitorAB.setMaxLength(2)
        self.txtResultVisitorAB.setAlignment(QtCore.Qt.AlignCenter)
        self.txtResultVisitorAB.setObjectName("txtResultVisitorAB")
        self.label_6 = QtWidgets.QLabel(self.tbAB)
        self.label_6.setGeometry(QtCore.QRect(760, 12, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.txtMessageAB = QtWidgets.QLineEdit(self.tbAB)
        self.txtMessageAB.setGeometry(QtCore.QRect(212, 50, 541, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.txtMessageAB.setFont(font)
        self.txtMessageAB.setText("")
        self.txtMessageAB.setMaxLength(150)
        self.txtMessageAB.setClearButtonEnabled(False)
        self.txtMessageAB.setObjectName("txtMessageAB")
        self.btnBackLocalAB = QtWidgets.QPushButton(self.tbAB)
        self.btnBackLocalAB.setGeometry(QtCore.QRect(100, 11, 31, 23))
        self.btnBackLocalAB.setObjectName("btnBackLocalAB")
        self.btnNextLocalAB = QtWidgets.QPushButton(self.tbAB)
        self.btnNextLocalAB.setGeometry(QtCore.QRect(210, 11, 31, 23))
        self.btnNextLocalAB.setObjectName("btnNextLocalAB")
        self.tbControls.addTab(self.tbAB, "")
        self.btnChange_Competition.raise_()
        self.lbl_background.raise_()
        self.btnChange_Background.raise_()
        self.lbl_logo_team_a.raise_()
        self.lbl_logo_team_b.raise_()
        self.lbl_league.raise_()
        self.lbl_vs.raise_()
        self.lbl_local.raise_()
        self.lbl_visitor.raise_()
        self.lbl_description.raise_()
        self.tbControls.raise_()
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
        self.tbControls.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UG Tweet Generator"))
        self.btnChange_Background.setText(_translate("MainWindow", "Cambiar fondo"))
        self.lbl_background.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_logo_team_a.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_logo_team_b.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_league.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_vs.setText(_translate("MainWindow", "VS"))
        self.lbl_local.setText(_translate("MainWindow", "0"))
        self.lbl_visitor.setText(_translate("MainWindow", "0"))
        self.btnChange_Competition.setText(_translate("MainWindow", "Cambiar competición"))
        self.btnBackLocalLV.setText(_translate("MainWindow", "<<"))
        self.btnNextLocalLV.setText(_translate("MainWindow", ">>"))
        self.label.setText(_translate("MainWindow", "LOCAL"))
        self.label_2.setText(_translate("MainWindow", "VISITANTE"))
        self.btnBackVisitorLV.setText(_translate("MainWindow", "<<"))
        self.btnNextVisitorLV.setText(_translate("MainWindow", ">>"))
        self.label_3.setText(_translate("MainWindow", "RESULTADO"))
        self.txtMessageLV.setPlaceholderText(_translate("MainWindow", "Escribe el mensaje que aparecerá en la imágen"))
        self.tbControls.setTabText(self.tbControls.indexOf(self.tbLV), _translate("MainWindow", "L - V"))
        self.btnBackVisitorAB.setText(_translate("MainWindow", "<<"))
        self.label_4.setText(_translate("MainWindow", "Equipo A"))
        self.btnNextVisitorAB.setText(_translate("MainWindow", ">>"))
        self.label_5.setText(_translate("MainWindow", "RESULTADO"))
        self.label_6.setText(_translate("MainWindow", "Equipo B"))
        self.txtMessageAB.setPlaceholderText(_translate("MainWindow", "Escribe el mensaje que aparecerá en la imágen"))
        self.btnBackLocalAB.setText(_translate("MainWindow", "<<"))
        self.btnNextLocalAB.setText(_translate("MainWindow", ">>"))
        self.tbControls.setTabText(self.tbControls.indexOf(self.tbAB), _translate("MainWindow", "A - B"))
        self.menuFile.setTitle(_translate("MainWindow", "Archivo"))
        self.actionConfiguration.setText(_translate("MainWindow", "Configuration"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

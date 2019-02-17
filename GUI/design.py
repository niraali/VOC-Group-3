# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Miles\Documents\Python Scripts\ExampleGUI\design.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(260, 180)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.priceBox = QtWidgets.QTextEdit(self.centralwidget)
        self.priceBox.setGeometry(QtCore.QRect(10, 40, 104, 31))
        self.priceBox.setObjectName("priceBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 13, 47, 20))
        self.label.setObjectName("label")
        self.taxRate = QtWidgets.QSpinBox(self.centralwidget)
        self.taxRate.setGeometry(QtCore.QRect(120, 40, 42, 22))
        self.taxRate.setProperty("value", 20)
        self.taxRate.setObjectName("taxRate")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 20, 47, 13))
        self.label_2.setObjectName("label_2")
        self.calcTaxButton = QtWidgets.QPushButton(self.centralwidget)
        self.calcTaxButton.setGeometry(QtCore.QRect(10, 80, 75, 23))
        self.calcTaxButton.setObjectName("calcTaxButton")
        self.resultsWindow = QtWidgets.QTextEdit(self.centralwidget)
        self.resultsWindow.setGeometry(QtCore.QRect(10, 110, 104, 31))
        self.resultsWindow.setObjectName("resultsWindow")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 260, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Price"))
        self.label_2.setText(_translate("MainWindow", "Tax Rate"))
        self.calcTaxButton.setText(_translate("MainWindow", "Calculate"))



# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Niraali Patel\Documents\VOC\Group 3 - House Price Predictor\GUI\Prediction.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1818, 1054)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 51, 151))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 160, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 15, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 51, 151))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 160, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 15, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 51, 151))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 160, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 234, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 234, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 15, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.typeOfHouseLabel = QtWidgets.QLabel(self.centralwidget)
        self.typeOfHouseLabel.setGeometry(QtCore.QRect(70, 60, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.typeOfHouseLabel.setFont(font)
        self.typeOfHouseLabel.setObjectName("typeOfHouseLabel")
        self.durationLabel = QtWidgets.QLabel(self.centralwidget)
        self.durationLabel.setGeometry(QtCore.QRect(70, 250, 80, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.durationLabel.setFont(font)
        self.durationLabel.setObjectName("durationLabel")
        self.newLabel = QtWidgets.QLabel(self.centralwidget)
        self.newLabel.setGeometry(QtCore.QRect(70, 330, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.newLabel.setFont(font)
        self.newLabel.setObjectName("newLabel")
        self.predictButton = QtWidgets.QPushButton(self.centralwidget)
        self.predictButton.setGeometry(QtCore.QRect(70, 430, 210, 60))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 217, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 140, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 217, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 217, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 217, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 140, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 217, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 217, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 140, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 217, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 140, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 140, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 140, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 217, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 217, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.predictButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.predictButton.setFont(font)
        self.predictButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.predictButton.setStyleSheet("background-color: rgb(111, 217, 255);")
        self.predictButton.setObjectName("predictButton")
        self.houseTypeLabel = QtWidgets.QLabel(self.centralwidget)
        self.houseTypeLabel.setGeometry(QtCore.QRect(70, 20, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.houseTypeLabel.setFont(font)
        self.houseTypeLabel.setObjectName("houseTypeLabel")
        self.specificHouseTitle = QtWidgets.QLabel(self.centralwidget)
        self.specificHouseTitle.setGeometry(QtCore.QRect(70, 530, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.specificHouseTitle.setFont(font)
        self.specificHouseTitle.setObjectName("specificHouseTitle")
        self.yearSoldInput = QtWidgets.QLineEdit(self.centralwidget)
        self.yearSoldInput.setGeometry(QtCore.QRect(70, 710, 210, 30))
        self.yearSoldInput.setStyleSheet("background-color: rgb(111, 217, 255);")
        self.yearSoldInput.setObjectName("yearSoldInput")
        self.requestLabel = QtWidgets.QLabel(self.centralwidget)
        self.requestLabel.setGeometry(QtCore.QRect(70, 610, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.requestLabel.setFont(font)
        self.requestLabel.setObjectName("requestLabel")
        self.yearSoldLabel = QtWidgets.QLabel(self.centralwidget)
        self.yearSoldLabel.setGeometry(QtCore.QRect(70, 670, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.yearSoldLabel.setFont(font)
        self.yearSoldLabel.setObjectName("yearSoldLabel")
        self.priceLabel = QtWidgets.QLabel(self.centralwidget)
        self.priceLabel.setGeometry(QtCore.QRect(70, 740, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.priceLabel.setFont(font)
        self.priceLabel.setObjectName("priceLabel")
        self.priceInput = QtWidgets.QLineEdit(self.centralwidget)
        self.priceInput.setGeometry(QtCore.QRect(70, 780, 210, 30))
        self.priceInput.setStyleSheet("background-color: rgb(111, 217, 255);")
        self.priceInput.setObjectName("priceInput")
        self.predictButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.predictButton_2.setGeometry(QtCore.QRect(70, 840, 210, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.predictButton_2.setFont(font)
        self.predictButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.predictButton_2.setStyleSheet("background-color: rgb(111, 217, 255);")
        self.predictButton_2.setObjectName("predictButton_2")
        self.specificSummary = QtWidgets.QLabel(self.centralwidget)
        self.specificSummary.setGeometry(QtCore.QRect(370, 890, 1421, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.specificSummary.setFont(font)
        self.specificSummary.setText("")
        self.specificSummary.setObjectName("specificSummary")
        self.disclaimerSign = QtWidgets.QLabel(self.centralwidget)
        self.disclaimerSign.setGeometry(QtCore.QRect(580, 950, 1191, 19))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.disclaimerSign.setFont(font)
        self.disclaimerSign.setObjectName("disclaimerSign")
        self.areaPrediction = MplWidget(self.centralwidget)
        self.areaPrediction.setGeometry(QtCore.QRect(300, 70, 1451, 771))
        self.areaPrediction.setObjectName("areaPrediction")
        self.postcodeInput = QtWidgets.QLineEdit(self.centralwidget)
        self.postcodeInput.setGeometry(QtCore.QRect(70, 210, 210, 30))
        self.postcodeInput.setStyleSheet("background-color: rgb(111, 217, 255);")
        self.postcodeInput.setObjectName("postcodeInput")
        self.durationLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.durationLabel_2.setGeometry(QtCore.QRect(70, 140, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.durationLabel_2.setFont(font)
        self.durationLabel_2.setObjectName("durationLabel_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 170, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.areaSummary = QtWidgets.QLabel(self.centralwidget)
        self.areaSummary.setGeometry(QtCore.QRect(370, 850, 1421, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.areaSummary.setFont(font)
        self.areaSummary.setText("")
        self.areaSummary.setObjectName("areaSummary")
        self.typeOfHouseInput = QtWidgets.QComboBox(self.centralwidget)
        self.typeOfHouseInput.setGeometry(QtCore.QRect(70, 100, 210, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.typeOfHouseInput.setFont(font)
        self.typeOfHouseInput.setStyleSheet("background-color: rgb(111, 217, 255);")
        self.typeOfHouseInput.setObjectName("typeOfHouseInput")
        self.typeOfHouseInput.addItem("")
        self.typeOfHouseInput.addItem("")
        self.typeOfHouseInput.addItem("")
        self.typeOfHouseInput.addItem("")
        self.typeOfHouseInput.addItem("")
        self.durationInput = QtWidgets.QComboBox(self.centralwidget)
        self.durationInput.setGeometry(QtCore.QRect(70, 290, 210, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.durationInput.setFont(font)
        self.durationInput.setStyleSheet("background-color: rgb(111, 217, 255);")
        self.durationInput.setObjectName("durationInput")
        self.durationInput.addItem("")
        self.durationInput.addItem("")
        self.durationInput.addItem("")
        self.newInput = QtWidgets.QComboBox(self.centralwidget)
        self.newInput.setGeometry(QtCore.QRect(70, 380, 210, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.newInput.setFont(font)
        self.newInput.setStyleSheet("background-color: rgb(111, 217, 255);")
        self.newInput.setObjectName("newInput")
        self.newInput.addItem("")
        self.newInput.addItem("")
        self.newInput.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.typeOfHouseInput, self.postcodeInput)
        MainWindow.setTabOrder(self.postcodeInput, self.durationInput)
        MainWindow.setTabOrder(self.durationInput, self.newInput)
        MainWindow.setTabOrder(self.newInput, self.predictButton)
        MainWindow.setTabOrder(self.predictButton, self.yearSoldInput)
        MainWindow.setTabOrder(self.yearSoldInput, self.priceInput)
        MainWindow.setTabOrder(self.priceInput, self.predictButton_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Prediction Prototype"))
        self.typeOfHouseLabel.setText(_translate("MainWindow", "Type of House"))
        self.durationLabel.setText(_translate("MainWindow", "Duration "))
        self.newLabel.setText(_translate("MainWindow", "Newly-built"))
        self.predictButton.setText(_translate("MainWindow", "Predict"))
        self.houseTypeLabel.setText(_translate("MainWindow", "Prediction for Same Type of House in Same Area"))
        self.specificHouseTitle.setText(_translate("MainWindow", "Estimation for \n"
"Specific House"))
        self.requestLabel.setText(_translate("MainWindow", "Please input information \n"
"from the most recent sale"))
        self.yearSoldLabel.setText(_translate("MainWindow", "Year sold"))
        self.priceLabel.setText(_translate("MainWindow", "Price"))
        self.predictButton_2.setText(_translate("MainWindow", "Estimate"))
        self.disclaimerSign.setText(_translate("MainWindow", "Disclaimer: This price is a guide, only taking price paid data into consideration. Please consult a local real estate professional or an appraiser for a second opinion."))
        self.durationLabel_2.setText(_translate("MainWindow", "Partial Postcode"))
        self.label_4.setText(_translate("MainWindow", "In the format: NG9 2EL"))
        self.typeOfHouseInput.setItemText(0, _translate("MainWindow", "Any"))
        self.typeOfHouseInput.setItemText(1, _translate("MainWindow", "Detatched"))
        self.typeOfHouseInput.setItemText(2, _translate("MainWindow", "Semi-detatched"))
        self.typeOfHouseInput.setItemText(3, _translate("MainWindow", "Terraced"))
        self.typeOfHouseInput.setItemText(4, _translate("MainWindow", "Flat"))
        self.durationInput.setItemText(0, _translate("MainWindow", "Freehold"))
        self.durationInput.setItemText(1, _translate("MainWindow", "Leasehold"))
        self.durationInput.setItemText(2, _translate("MainWindow", "Any"))
        self.newInput.setItemText(0, _translate("MainWindow", "Yes"))
        self.newInput.setItemText(1, _translate("MainWindow", "No"))
        self.newInput.setItemText(2, _translate("MainWindow", "Any"))


from GUI.models.mplwidget import MplWidget

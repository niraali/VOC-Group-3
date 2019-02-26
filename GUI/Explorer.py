# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Niraali Patel\Documents\VOC\Group 3 - House Price Predictor\GUI\Explorer.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1009, 710)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fileSelector = QtWidgets.QPushButton(self.centralwidget)
        self.fileSelector.setGeometry(QtCore.QRect(20, 20, 112, 34))
        self.fileSelector.setObjectName("fileSelector")
        self.enterButton = QtWidgets.QPushButton(self.centralwidget)
        self.enterButton.setGeometry(QtCore.QRect(20, 260, 112, 34))
        self.enterButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.enterButton.setObjectName("enterButton")
        self.countyDropDown = QtWidgets.QComboBox(self.centralwidget)
        self.countyDropDown.setGeometry(QtCore.QRect(20, 90, 111, 31))
        self.countyDropDown.setEditable(False)
        self.countyDropDown.setCurrentText("")
        self.countyDropDown.setObjectName("countyDropDown")
        self.countyDropDown.addItem("")
        self.countyDropDown.setItemText(0, "")
        self.countyDropDown.addItem("")
        self.houseNoInput = QtWidgets.QLineEdit(self.centralwidget)
        self.houseNoInput.setGeometry(QtCore.QRect(20, 160, 113, 25))
        self.houseNoInput.setObjectName("houseNoInput")
        self.postcodeInput = QtWidgets.QLineEdit(self.centralwidget)
        self.postcodeInput.setGeometry(QtCore.QRect(20, 220, 113, 25))
        self.postcodeInput.setObjectName("postcodeInput")
        self.houseNoLabel = QtWidgets.QLabel(self.centralwidget)
        self.houseNoLabel.setGeometry(QtCore.QRect(20, 130, 121, 19))
        self.houseNoLabel.setObjectName("houseNoLabel")
        self.postcodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.postcodeLabel.setGeometry(QtCore.QRect(40, 190, 68, 19))
        self.postcodeLabel.setObjectName("postcodeLabel")
        self.countyLabel = QtWidgets.QLabel(self.centralwidget)
        self.countyLabel.setGeometry(QtCore.QRect(30, 60, 68, 19))
        self.countyLabel.setObjectName("countyLabel")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(170, 21, 771, 281))
        self.tableView.setObjectName("tableView")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.fileSelector.setText(_translate("mainWindow", "Choose File"))
        self.enterButton.setText(_translate("mainWindow", "Enter"))
        self.countyDropDown.setItemText(1, _translate("mainWindow", "NOTTINGHAMSHIRE"))
        self.houseNoLabel.setText(_translate("mainWindow", "House Number"))
        self.postcodeLabel.setText(_translate("mainWindow", "Postcode"))
        self.countyLabel.setText(_translate("mainWindow", "County"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

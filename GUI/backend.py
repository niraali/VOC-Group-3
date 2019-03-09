# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 14:29:59 2019

@author: Niraali
"""

# Before running anything, you need to install PyQt5. Do this by running
# "pip install pyqt5" in your command line. If you don't none of this will 
# work.

import sys, os
from PyQt5 import QtWidgets, QtCore
import GUI.ActualFilter as filters
import GUI.models.dataframe_model as dm
from prototype import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd
import numpy as np

# In QT-Designer (you can find it in C:\Anaconda\Library\bin\designer.exe) you
# can create a UI with drag and drop. When you save this, a .ui file is created.
# When you run "pyuic5 mydesign.ui -o mydesign.py" in a command line window
# (making sure the file names and paths are correct) it will convert it to a
# python file. You can see this has been done with 'design.ui' converted to
# 'design.py'. You can then use this as shown in this file.
from GUI.Explorer import Ui_mainWindow as ExplorerUI
from GUI.Prediction import Ui_MainWindow as PredictionUI

selectedFile = ""
xs = 0
ys = 0
predict_x = 0
predict_y = 0
regression_line = 0

class DataExplorer(QtWidgets.QMainWindow):
    listOfCheckboxes = []
    listOfDistricts = ["Ashfield", "Bassetlaw", "Broxtowe", "Gedling", "Mansfield", "Newark and Sherwood",
                       "Nottingham", "Rushcliffe"]

    # This is just to initialise the window. It links all the UI elements to
    # the python script and 'connects' the calcButtonClicked function to the
    # actual button, so it performs that action.
    def __init__(self):
        super(DataExplorer, self).__init__()
        self.ui = ExplorerUI()
        self.ui.setupUi(self)
        self.listOfCheckboxes = [self.ui.ashfieldCheck, self.ui.bassetlawCheck, self.ui.broxtoweCheck,
                                 self.ui.gedlingCheck, self.ui.mansfieldCheck, self.ui.newarkCheck,
                                 self.ui.nottinghamCheck, self.ui.rushcliffeCheck]
        self.ui.fileSelector.clicked.connect(self.openFileDialogue)
        self.ui.enterButton.clicked.connect(self.enterButton)
        self.ui.enterButton2.clicked.connect(self.showAvgPrices)
        self.ui.predictionPrototypeButton.clicked.connect(self.goToPredictionPrototype)

    def goToPredictionPrototype(self):
        if self.checkValidFile():
            predictionWindow.show()

    def checkValidFile(self):
        if not os.path.exists(selectedFile):
            msg = QtWidgets.QMessageBox().critical(self, 'Important Message', "Please select a valid file",
                                                   QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
            return False
        return True

    def displayAveragePricesChart(self, dataframe):
        self.ui.mplDistrict.canvas.ax.clear()
        self.ui.mplDistrict.canvas.ax.bar(np.arange(len(dataframe)), dataframe['Avg Price (£)'],
                                          tick_label=dataframe['District'].str[:3])
        self.ui.mplDistrict.canvas.ax.set_xlabel('District')
        self.ui.mplDistrict.canvas.ax.set_ylabel('Average Price')
        self.ui.mplDistrict.canvas.draw()

    def displaySpecificPricesChart(self, dataframe):
        self.ui.mplSpecific.canvas.ax.clear()
        self.ui.mplSpecific.canvas.ax.plot(dataframe['Year Sold'], dataframe['Present Value (GBP)'], marker='o')
        self.ui.mplSpecific.canvas.draw()
        self.ui.mplSpecific.canvas.ax.set_xlabel('Year')
        self.ui.mplSpecific.canvas.ax.set_ylabel('Price')

    def openFileDialogue(self):
        global selectedFile
        selectedFile, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select CSV", "", "CSV Files (*.csv)")

    def enterButton(self):
        county = str(self.ui.countyDropDown.currentText())
        houseNumber = self.ui.houseNoInput.text()
        postcode = self.ui.postcodeInput.text().upper()
        if (county == ""):
            msg = QtWidgets.QMessageBox().critical(self, 'Important Message', "Please select a County",
                                                   QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
            return

        if (postcode == ""):
            msg = QtWidgets.QMessageBox().critical(self, 'Important Message', "Please enter a Postcode",
                                                   QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
            return

        if not self.checkValidFile():
            return

        filtered_data = filters.filterByProperty(county, postcode, houseNumber, selectedFile)

        if filtered_data.empty:
            msg = QtWidgets.QMessageBox().critical(self, 'Important Message', "No properties match selected filter",
                                                   QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
            return

        print(filtered_data)
        dataModel = dm.PandasModel(filtered_data)
        self.ui.tableViewer.setModel(dataModel)
        if filtered_data['Postcode'].unique().size == 1:
            self.displaySpecificPricesChart(filtered_data)

    def showAvgPrices(self):
        #[(0, box1), (1, box2), (2, box3)]
        if not self.checkValidFile():
            return

        avgPriceDf = pd.DataFrame(columns=['District', 'Avg Price (£)'])
        avgPriceList = []
        districtsUsed = []
        for index, box in enumerate(self.listOfCheckboxes):
            if box.isChecked():
                filtered_data = filters.filterByDistrict(self.listOfDistricts[index].upper(), selectedFile)
                avg = filtered_data['Price (GBP)'].astype(float).mean()
                avgPriceList.append(avg)
                districtsUsed.append(self.listOfDistricts[index])

        if not avgPriceList:
            msg = QtWidgets.QMessageBox().critical(self, 'Important Message', "No areas selected",
                                                   QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
            return

        avgPriceDf['District'] = districtsUsed
        avgPriceDf['Avg Price (£)'] = avgPriceList

        #Print avgPriceDf to table view
        dataModel = dm.PandasModel(avgPriceDf)
        self.ui.tableViewer.setModel(dataModel)
        self.displayAveragePricesChart(avgPriceDf)

class PredictionPrototype(QtWidgets.QMainWindow):
    def __init__(self):
        super(PredictionPrototype, self).__init__()
        self.ui = PredictionUI()
        self.ui.setupUi(self)
        self.ui.predictButton.clicked.connect(self.predictButton)
        self.ui.predictButton_2.clicked.connect(self.predictButton_2)

    def predictButton(self):
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        global xs, ys, predict_x, predict_y, regression_line

        typeOfHouse = str(self.ui.typeOfHouseInput.currentText())[:1]
        duration = str(self.ui.durationInput.currentText())[:1]
        new = str(self.ui.newInput.currentText())[:1]
        postcode_input = self.ui.postcodeInput.text().upper()

        if typeOfHouse == 'A':
            typeOfHouse = ""
        if duration == 'A':
            duration = ""
        if new == 'A':
            new = ""

        try:
            setupData(selectedFile, new, duration, typeOfHouse, postcode_input)
        except RuntimeError as err:
            print("d")
            msg = QtWidgets.QMessageBox().critical(self, 'Important Message', str(err),
                                                   QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
            return

        xs, ys, predict_x, predict_y, regression_line = prototype()
        self.areaPrediction(xs, ys, predict_x, predict_y, regression_line)
        if (postcode_input):
            text = str(postcode_input) + ": In this area "
        else:
            text = "Over all areas "

        text += "the average price for a property is £" + str('{:.2f}'.format(round(predict_y, 2)))
        self.ui.areaSummary.setText(text)

        QtWidgets.QApplication.restoreOverrideCursor()

    def predictButton_2(self):
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        priceInput = self.ui.priceInput.text()
        yearSoldInput = self.ui.yearSoldInput.text()
        predictHouse = button2(priceInput, yearSoldInput)
        self.specificHousePrediction(predictHouse, int(yearSoldInput), float(priceInput))

        text = "This property would be valued at £" + str('{:.2f}'.format(round(predictHouse, 2)))
        self.ui.specificSummary.setText(text)

        QtWidgets.QApplication.restoreOverrideCursor()

    def areaPrediction(self, xs, ys, predict_x, predict_y, regression_line):
        self.ui.areaPrediction.canvas.ax.clear()
        self.ui.areaPrediction.canvas.ax.scatter(xs, ys, color='b', label = '')
        self.ui.areaPrediction.canvas.ax.scatter(predict_x, predict_y, color='g', label='Area prediction')
        self.ui.areaPrediction.canvas.ax.plot(xs, regression_line, label='Regression line')
        self.ui.areaPrediction.canvas.ax.set_xlabel('Year')
        self.ui.areaPrediction.canvas.ax.set_ylabel('Price')
        self.ui.areaPrediction.canvas.ax.legend()
        self.ui.areaPrediction.canvas.ax.grid(False)
        self.ui.areaPrediction.canvas.draw()

    def specificHousePrediction(self, predict_house, year_input, price_input):
        global xs, ys, predict_x, predict_y, regression_line
        self.areaPrediction(xs, ys, predict_x, predict_y, regression_line)
        self.ui.areaPrediction.canvas.ax.scatter(year_input, price_input, color='#ff1493', label='Previous sale')
        self.ui.areaPrediction.canvas.ax.scatter(2019, predict_house, color='#ff1493', label='New prediction')
        self.ui.areaPrediction.canvas.ax.legend()
        self.ui.areaPrediction.canvas.ax.grid(False)
        self.ui.areaPrediction.canvas.draw()


app = QtWidgets.QApplication([])
window = DataExplorer()
predictionWindow = PredictionPrototype()
window.show() # Here is where the UI is shown.
sys.exit(app.exec()) # When the X button is pressed, this will close the app.
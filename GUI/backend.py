# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 19:29:59 2019

@author: Niraali
"""

# Before running anything, you need to install PyQt5. Do this by running
# "pip install pyqt5" in your command line. If you don't none of this will 
# work.

import sys
from PyQt5 import QtWidgets
import GUI.ActualFilter as filters
import GUI.models.dataframe_model as dm
import matplotlib.pyplot as plt
import numpy as np

# In QT-Designer (you can find it in C:\Anaconda\Library\bin\designer.exe) you 
# can create a UI with drag and drop. When you save this, a .ui file is created.
# When you run "pyuic5 mydesign.ui -o mydesign.py" in a command line window 
# (making sure the file names and paths are correct) it will convert it to a 
# python file. You can see this has been done with 'design.ui' converted to 
# 'design.py'. You can then use this as shown in this file.
from GUI.Explorer import Ui_mainWindow

class DataExplorer(QtWidgets.QMainWindow):
    selectedFile = ""
    listOfCheckboxes = []
    listOfDistricts = ["Ashfield", "Bassetlaw", "Broxtowe", "Gedling", "Mansfield", "Newark and Sherwood",
                       "Nottingham", "Rushcliffe"]

    # This is just to initialise the window. It links all the UI elements to
    # the python script and 'connects' the calcButtonClicked function to the 
    # actual button, so it performs that action.
    def __init__(self):
        super(DataExplorer, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        #self.listOfCheckboxes = [self.ui.ashfieldCheck, self.bassetlawCheck, self.broxtoweCheck, self.gedlingCheck,
                                 #self.mansfieldCheck, self.newarkCheck, self.nottingham, self.rushcliffe]
        self.ui.fileSelector.clicked.connect(self.openFileDialogue)
        self.ui.enterButton.clicked.connect(self.enterButton)
        #self.ui.ashfieldCheck.stateChanged.connect(self.showAvgPrices)
        #self.ui.bassetlawCheck.stateChanged.connect(self.showAvgPrices)
        #self.ui.broxtoweCheck.stateChanged.connect(self.showAvgPrices)
        #self.ui.gedlingCheck.stateChanged.connect(self.showAvgPrices)
        #self.ui.mansfieldCheck.stateChanged.connect(self.showAvgPrices)
        #self.ui.newarkCheck.stateChanged.connect(self.showAvgPrices)
        #self.ui.nottinghamCheck.stateChanged.connect(self.showAvgPrices)
        #self.ui.rushcliffeCheck.stateChanged.connect(self.showAvgPrices)

    def openFileDialogue(self):
        self.selectedFile, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select CSV", "","CSV Files (*.csv)")

    def enterButton(self):
        county = str(self.ui.countyDropDown.currentText())
        houseNumber = self.ui.houseNoInput.text()
        postcode = self.ui.postcodeInput.text()
        if (county != ""):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Please select a county")
        if (postcode != ""):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Please input a Postcode")
        filtered_data = filters.filterByProperty(county, postcode, houseNumber, self.selectedFile)
        print(filtered_data)
        dataModel = dm.PandasModel(filtered_data)
        self.ui.tableView.setModel(dataModel)

    #def showAvgPrices(self):
     #   listOfAvgPrices = []     #[ (0, box1), (1, box2), (2, box3) ]
      #  for index, box in enumerate(self.listOfCheckboxes):
       #     if box.isChecked():
        #        filtered_data = filters.filterByDistrict(self.listOfDistricts[index].upper(), self.selectedFile)
         #       listOfAvgPrices.append(self.calculateAvgPrice(filtered_data))

        #Print listOfAvgPrices to table view

   # def calculateAvgPrice(self, dataframe):
        #avg =
        #return avg


#print ("calculate an average of first n natural numbers")
#n = input("Enter Number ")
#n = int (n)
#average = 0
#sum = 0
#for num in range(0,n+1,1):
 #   sum = sum+num;
#average = sum / n
#print("Average of first ", n, "number is: ", average)


app = QtWidgets.QApplication([]) # Boilerplate code, don't worry about this.
window = DataExplorer()
window.show() # Here is where the UI is shown.
sys.exit(app.exec()) # When the X button is pressed, this will close the app.
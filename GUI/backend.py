# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 19:29:59 2019

@author: Miles
"""

# Before running anything, you need to install PyQt5. Do this by running
# "pip install pyqt5" in your command line. If you don't none of this will 
# work.

import sys
from PyQt5 import QtWidgets

# In QT-Designer (you can find it in C:\Anaconda\Library\bin\designer.exe) you 
# can create a UI with drag and drop. When you save this, a .ui file is created.
# When you run "pyuic5 mydesign.ui -o mydesign.py" in a command line window 
# (making sure the file names and paths are correct) it will convert it to a 
# python file. You can see this has been done with 'design.ui' converted to 
# 'design.py'. You can then use this as shown in this file.
from design import Ui_MainWindow

class TaxCalc(QtWidgets.QMainWindow):
    # This is just to initialise the window. It links all the UI elements to
    # the python script and 'connects' the calcButtonClicked function to the 
    # actual button, so it performs that action.
    def __init__(self):
        super(TaxCalc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.calcTaxButton.clicked.connect(self.calcButtonClicked)
    
    # This function displays the price with tax added on.
    def calcButtonClicked(self):
        price = self.ui.priceBox.toPlainText() # Grabs the text from the textbox
        percent = self.ui.taxRate.value() / 100 # Grabs the value from the spinner and converts it to a percentage
        total = int(price) * (1 + percent) # Calculates the total price      
        self.ui.resultsWindow.setText(str(total)) # Sets the text of the resultBox to be the total as a string.

app = QtWidgets.QApplication([]) # Boilerplate code, don't worry about this.
window = TaxCalc() # Creates a new TaxCalc window (the name of the class we make above)
window.show() # Here is where the UI is shown.
sys.exit(app.exec()) # When the X button is pressed, this will close the app.
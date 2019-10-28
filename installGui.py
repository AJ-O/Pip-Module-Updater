import sys
import os

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QCheckBox, QTableWidget
from PyQt5.QtWidgets import QGroupBox, QLabel, QPushButton, QFormLayout, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import Qt, QCoreApplication
from checkPipFiles import moduleCheck

LastStateRole = Qt.UserRole

class App(QWidget):

    def __init__(self):

        super().__init__()
        self.title = "Pip Module Checker"
        self.top = 200
        self.left = 500
        self.width = 600
        self.height = 300
        self.indices = []
        self.chkBoxItem = []
        self.data = moduleCheck()#getting data from the checkPipFiles file
        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()#to create a table that will store the module name, older version, new version and a check box to download or not

        self.layout = QVBoxLayout()#table is added into it
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        button = QPushButton('All selected', self)#when the user is finished selecting the modules they want to update
        button.move(450, 150)
        button.clicked.connect(self.on_done)
        self.show()


    def createTable(self):

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(self.data[0]))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Module Name", "Old Version", "New Version", "Download?"])

        #setting the table with data received via moduleCheck function
        for i in range(len(self.data[0])):

            self.tableWidget.setItem(i, 0, QTableWidgetItem(self.data[0][i]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(self.data[1][i]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(self.data[2][i]))

            #Creating a checkbox of type QTableWidgetItem
            self.chkBoxItem.append(QTableWidgetItem())
            self.chkBoxItem[i].setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            self.chkBoxItem[i].setCheckState(Qt.Unchecked)
            self.tableWidget.setItem(i, 3, self.chkBoxItem[i])

    #function to check those modules that the user has selected that they want to update
    def on_done(self):

        for i in range(len(self.chkBoxItem)):

            val = self.chkBoxItem[i].checkState()

            if val == 2:#if checkbox is checked

                self.indices.append(i)

        for i in self.indices:

            print("selected modules to update: ", self.data[0][i])

        self.installModules(self.indices)

    #Update the selected modules
    def installModules(self, indices):

        for i in indices:

            moduleName = self.data[0][i]
            os.system('pip3 uninstall ' + moduleName)
            os.system('pip3 install ' + moduleName)

        print("Latest updated modules: \n")
        os.system('pip3 list --format=json')
        QCoreApplication.instance().quit()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

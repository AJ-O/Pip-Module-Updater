from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QCheckBox, QTableWidget
from PyQt5.QtWidgets import QGroupBox, QLabel, QPushButton, QFormLayout, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import Qt
import sys

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
        self.data = [['asn1crypto', 'astroid', 'certifi', 'chardet', 'command-not-found', 'cryptography', 'defer', 'distro-info', 'idna',
        'isort', 'keyring', 'keyrings.alt', 'language-selector', 'lazy-object-proxy', 'lightdm-gtk-greeter-settings', 'mccabe', 'netifaces', 'pexpect', 'Pillow',
        'pip', 'pycairo', 'pycrypto', 'pycups', 'pygobject', 'pylint', 'python-apt', 'python-dateutil', 'python-debian', 'pyxdg', 'PyYAML', 'reportlab',
        'requests', 'requests-unixsocket', 'SecretStorage', 'selenium', 'setuptools', 'six', 'typed-ast', 'ubuntu-drivers-common',
        'ufw', 'urllib3', 'usb-creator', 'wheel', 'wrapt', 'xkit'], ['0.24.0', '2.3.2', '2019.9.11', '3.0.4', '0.3', '2.1.4', '1.0.6', '0.18ubuntu0.18.04.1',
        '2.8', '4.3.21', '10.6.0', '3.0', '0.1', '1.4.2', '1.2.2', '0.6.1', '0.10.4', '4.2.1', '5.1.0', '9.0.1', '1.16.2', '2.6.1', '1.9.73', '3.26.1',
         '2.4.3', '1.6.4', '2.6.1', '0.1.32', '0.25', '3.12', '3.4.0', '2.22.0', '0.1.5', '2.3.1', '3.141.0', '39.0.1', '1.12.0', '1.4.0', '0.0.0', '0.36',
          '1.25.6', '0.3.3', '0.30.0', '1.11.2', '0.0.0'], ['0.24.0', '2.3.2', '2019.9.11', '3.0.4', '0.3', '2.1.4', '1.0.6', '0.18ubuntu0.18.04.1',
          '2.8', '4.3.21', '10.6.0', '3.0', '0.1', '1.4.2', '1.2.2', '0.6.1', '0.10.4', '4.2.1', '5.1.0', '9.0.1', '1.16.2', '2.6.1', '1.9.73', '3.26.1',
           '2.4.3', '1.6.4', '2.6.1', '0.1.32', '0.25', '3.12', '3.4.0', '2.22.0', '0.1.5', '2.3.1', '3.141.0', '39.0.1', '1.12.0', '1.4.0', '0.0.0', '0.36',
            '1.25.6', '0.3.3', '0.30.0', '1.11.2', '0.0.0']]
        self.initUI()

    def initUI(self):

        #self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        button = QPushButton('All selected', self)
        button.move(450, 150)
        button.clicked.connect(self.on_done)
        self.show()

    def on_done(self):

        #self.tableWidget.cellChanged.connect(self.onCellChanged)
        for i in range(len(self.chkBoxItem)):

            val = self.chkBoxItem[i].checkState()

            if val == 2:

                self.indices.append(i)

        print(self.indices)

        for i in self.indices:

            print("selected: ", self.data[0][i])

        print('Done selected!')


    def createTable(self):



        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(self.data[0]))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Module Name", "Old Version", "New Version", "Download?"])

        for i in range(len(self.data[0])):

            self.tableWidget.setItem(i, 0, QTableWidgetItem(self.data[0][i]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(self.data[1][i]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(self.data[2][i]))

            self.chkBoxItem.append(QTableWidgetItem())
            self.chkBoxItem[i].setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            self.chkBoxItem[i].setCheckState(Qt.Unchecked)
            self.tableWidget.setItem(i, 3, self.chkBoxItem[i])

        #self.tableWidget.resizeColumnsToContents() -- resizing columns dynamically
        #self.tableWidget.cellChanged.connect(self.onCellChanged)
    def createCbButton(self):

        rb = QCheckBox('Test', self)

        rb.toggled.connect(self.checkState)

    def checkState(self):

        rb = self.sender()

        if rb.isChecked():

            print('checked!')

    # def onCellChanged(self, row, column):
    #
    #     item = self.tableWidget.item(row, column)
    #     lastState = item.data(LastStateRole)
    #     currentState = item.checkState()
    #     mname = self.tableWidget.itemAt(row, column)
    #     print(mname.text())
    #
    #     if currentState != lastState:
    #
    #         if currentState == Qt.Checked:
    #
    #             self.li.append(mname.text())
    #
    #         else:
    #
    #             self.li.remove(mname.text())
    #
    #         item.setData(LastStateRole, currentState)

        #print(self.li)

    # def on_click(self):
    #
    #     print("\n")
    #
    #     for currentQTableWidgetItem in self.tableWidget.selectedItems():
    #
    #         print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

if __name__  == "__main__":

    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())

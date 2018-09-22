import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Ui_WeekTable import *
from MainWindow import *
sys.path.append("..")
from func.login_test import *
#from PyQt5 import QtCore, QtGui, QtWidgets


class WeekTable(QMainWindow,  Ui_WeekTable):
    def __init__(self,  parent=None):
        super(WeekTable,  self).__init__(parent)
        self.setupUi(self)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = WeekTable()
    myWin.show()
    sys.exit(app.exec_())

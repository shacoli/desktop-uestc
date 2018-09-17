import sys
import config
from PyQt5.QtWidgets import *
from Ui_login import *
from Ui_WeekTable import *

class WeekTable(QMainWindow,  Ui_WeekTable):
    def __init__(self,  parent=None):
        super(WeekTable,  self).__init__(parent)
        self.setupUi(self)

  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = WeekTable()
    myWin.show()
    sys.exit(app.exec_())

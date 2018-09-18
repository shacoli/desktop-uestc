import sys
import config
from PyQt5.QtWidgets import *
from Ui_login import *
from Ui_WeekTable import *
sys.path.append("..")
from funcs import *

class WeekTable(QMainWindow,  Ui_WeekTable):
    def __init__(self,  parent=None):
        super(WeekTable,  self).__init__(parent)
        self.setupUi(self)
        
        self.switch_button.clicked.connect(self.get_day_table)

    def get_day_table(self):
        day = self.dateEdit.date().day()
        month = self.dateEdit.date().month()
        year = self.dateEdit.date().year()
	
    def get_table_again(self):
        get_table()
        get_day_table()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = WeekTable()
    myWin.show()
    sys.exit(app.exec_())

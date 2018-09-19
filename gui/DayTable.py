import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from Ui_login import *
from Ui_DayTable import *
sys.path.append("..")
from funcs import get_table

class DayTable(QMainWindow,  Ui_DayTable):
    def __init__(self,  parent=None):
        super(DayTable,  self).__init__(parent)
        self.setupUi(self)
        
        self.dateEdit.setDate(QDate.currentDate())
        
        self.broadcast_label.setText("")
        self.switch_button.clicked.connect(self.get_day_table)
        self.rescrap_button.clicked.connect(self.get_table_again)
        self.day = self.dateEdit.date().day()
        self.month = self.dateEdit.date().month()
        self.year = self.dateEdit.date().year()
    
    def get_day_table(self):
        #self.scrollAreaWidgetContents.setMinimumHeight(1800)
        pass
    
    def get_table_again(self):
        self.broadcast_label.setText("重新抓取用时为 %1.5f" %float(get_table.write_in_my_table(2017030102012, "402561")))
        self.get_day_table()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = DayTable()
    myWin.show()
    sys.exit(app.exec_())

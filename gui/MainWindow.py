import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from Ui_MainWindow import *
from WeekTable import  *
from login import *

class CallMainWindow(QMainWindow, Ui_Main_Window):
	def __init__(self, parent = None):
		super(CallMainWindow, self).__init__(parent)
		self.setupUi(self)
		self.dayTable.setText("日课程表")
		self.dayTable.clicked.connect(self.ShowDayTable)
		self.menu.triggered[QAction].connect(self.Login)
        
	def ShowDayTable(self):
		DayTable.show()
		
	def Login(self):
		LoginWin.show()

        
class Table(QWidget):
    
    def __init__(self,  arg = None):
        super(Table, self).__init__(arg)
        self.setWindowTitle("Qtable example")
        self.resize(500, 300)
        self.model = QStandardItemModel(4, 4)
        self.model.setHorizontalHeaderLabels(['1', '2', '3', '4'])
        
        self.tableView = QTableView()
        self.tableView.setModel(self.model)
        
        dlgLayout = QVBoxLayout();
        dlgLayout.addWidget(self.tableView)
        self.setLayout(dlgLayout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = CallMainWindow()
    mainWin.show()
    DayTable = WeekTable()
    LoginWin = MyLogin()
    sys.exit(app.exec_())

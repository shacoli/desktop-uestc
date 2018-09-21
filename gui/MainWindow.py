import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from Ui_MainWindow import *
from DayTable import  *
from WeekTable import *
from LoginSuccess import *
from Login import *

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		self.dayTable.setText("日课程表")
		self.dayTable.clicked.connect(self.ShowDayTable)
		self.weekTable.clicked.connect(self.ShowWeekTable)
		self.menu.triggered[QAction].connect(self.Login)
        
	def ShowDayTable(self):
		Day_Table.show()
		
	def ShowWeekTable(self):
		Week_Table.show()
	
	def Login(self):
		LoginWin.show()
			

        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    Day_Table = DayTable()
    Week_Table = WeekTable()
    LoginWin = Login()
    login_success_win = LoginSuccess()
    sys.exit(app.exec_())

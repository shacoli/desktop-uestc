import sys
import config
from PyQt5.QtWidgets import *
from Ui_login import *
from MainWindow import *
sys.path.append("..")
from funcs.login_test import *
#from PyQt5 import QtCore, QtGui, QtWidgets


class MyLogin(QMainWindow,  Ui_LoginWindow):
    def __init__(self,  parent=None):
        super(MyLogin,  self).__init__(parent)
        self.setupUi(self)
        
        
        self.loginButton.clicked.connect(self.Login)
        self.touristButton.clicked.connect(self.TourLogin)
        
    def Login(self):
        a = self.LoginAccount.text()
        b = self.LoginPassword.text()
        if(login_test(a, b) == True):
            print("登陆成功！！")
        else:
            pass
        #MainWin.show()
        myWin.close()
            
    def TourLogin(self):
        #MainWin.show()
        myWin.close()
            
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyLogin()
    myWin.show()
    sys.exit(app.exec_())

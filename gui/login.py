import sys
from PyQt5.QtWidgets import *
from Ui_login import *
from MainWindow import *
from login_success import *
sys.path.append("..")
from funcs.login_test import *
#from PyQt5 import QtCore, QtGui, QtWidgets


class MyLogin(QMainWindow,  Ui_LoginWindow):
    def __init__(self,  parent=None):
        super(MyLogin,  self).__init__(parent)
        self.setupUi(self)
        
        self.error_label.setText("")
        
        self.loginButton.clicked.connect(self.Login_Test)
        self.touristButton.clicked.connect(self.TourLogin)
        
        self.login_success_win = LoginSuccess()
        #self.myWin = MyLogin()
		
    def Login_Test(self):
        a = self.LoginAccount.text()
        b = self.LoginPassword.text()
        
        if(login_test(a, b) == True):
            #print("登陆成功！！")
            
            self.login_success_win.show()
            self.close()
        else:
            self.error_label.setText("用户名或密码错误！")
        #myWin.close()
        #self.close()
            
    def TourLogin(self):
        myWin.close()
            
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyLogin()
    myWin.show()
    login_success_win = LoginSuccess()
    sys.exit(app.exec_())

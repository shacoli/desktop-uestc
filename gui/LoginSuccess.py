import sys
from PyQt5.QtWidgets import *
from Ui_LoginSuccess import *
#from PyQt5 import QtCore, QtGui, QtWidgets


class LoginSuccess(QMainWindow,  Ui_LoginSuccess):
    def __init__(self,  parent=None):
        super(LoginSuccess,  self).__init__(parent)
        self.setupUi(self)
        self.okButton.setText("好")
        self.okButton.clicked.connect(self.ok)

    def ok(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = LoginSuccess()
    myWin.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/shacoli/open-project/desktop-uestc/gui/login_success.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginSuccess(object):
    def setupUi(self, LoginSuccess):
        LoginSuccess.setObjectName("LoginSuccess")
        LoginSuccess.resize(324, 94)
        self.widget = QtWidgets.QWidget(LoginSuccess)
        self.widget.setGeometry(QtCore.QRect(80, 20, 168, 56))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.okButton = QtWidgets.QPushButton(self.widget)
        self.okButton.setObjectName("okButton")
        self.verticalLayout.addWidget(self.okButton)

        self.retranslateUi(LoginSuccess)
        QtCore.QMetaObject.connectSlotsByName(LoginSuccess)

    def retranslateUi(self, LoginSuccess):
        _translate = QtCore.QCoreApplication.translate
        LoginSuccess.setWindowTitle(_translate("LoginSuccess", "Form"))
        self.label.setText(_translate("LoginSuccess", "登陆成功！！"))
        self.okButton.setText(_translate("LoginSuccess", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginSuccess = QtWidgets.QWidget()
    ui = Ui_LoginSuccess()
    ui.setupUi(LoginSuccess)
    LoginSuccess.show()
    sys.exit(app.exec_())


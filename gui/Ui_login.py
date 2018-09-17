# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\小汇总\eric_project\uestc_pro_1\login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(480, 320)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        LoginWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 60, 151, 171))
        self.graphicsView.setObjectName("graphicsView")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(200, 80, 202, 134))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.LoginAccount = QtWidgets.QLineEdit(self.layoutWidget)
        self.LoginAccount.setObjectName("LoginAccount")
        self.verticalLayout_2.addWidget(self.LoginAccount)
        self.LoginPassword = QtWidgets.QLineEdit(self.layoutWidget)
        self.LoginPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LoginPassword.setObjectName("LoginPassword")
        self.verticalLayout_2.addWidget(self.LoginPassword)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.loginButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout_4.addWidget(self.loginButton)
        self.touristButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.touristButton.setObjectName("touristButton")
        self.verticalLayout_4.addWidget(self.touristButton)
        self.splitter.raise_()
        self.graphicsView.raise_()
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 23))
        self.menubar.setObjectName("menubar")
        self.menu_S = QtWidgets.QMenu(self.menubar)
        self.menu_S.setObjectName("menu_S")
        self.menu_T = QtWidgets.QMenu(self.menubar)
        self.menu_T.setObjectName("menu_T")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)
        self.action_EXCEL = QtWidgets.QAction(LoginWindow)
        self.action_EXCEL.setObjectName("action_EXCEL")
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_T.menuAction())
        self.menubar.addAction(self.menu_S.menuAction())

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.label.setText(_translate("LoginWindow", "学号"))
        self.label_2.setText(_translate("LoginWindow", "密码"))
        self.loginButton.setText(_translate("LoginWindow", "连接"))
        self.touristButton.setText(_translate("LoginWindow", "游客模式"))
        self.menu_S.setTitle(_translate("LoginWindow", "支持(S)"))
        self.menu_T.setTitle(_translate("LoginWindow", "工具(T)"))
        self.menu_F.setTitle(_translate("LoginWindow", "文件(&F)"))
        self.action_EXCEL.setText(_translate("LoginWindow", "导出为EXCEL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())


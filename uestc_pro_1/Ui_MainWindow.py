# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\小汇总\eric_project\uestc_pro_1\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main_Window(object):
    def setupUi(self, Main_Window):
        Main_Window.setObjectName("Main_Window")
        Main_Window.resize(817, 573)
        self.centralwidget = QtWidgets.QWidget(Main_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.dayTable = QtWidgets.QPushButton(self.centralwidget)
        self.dayTable.setGeometry(QtCore.QRect(90, 60, 151, 101))
        self.dayTable.setObjectName("dayTable")
        self.weekTable = QtWidgets.QPushButton(self.centralwidget)
        self.weekTable.setGeometry(QtCore.QRect(260, 60, 151, 101))
        self.weekTable.setObjectName("weekTable")
        Main_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 817, 23))
        self.menubar.setObjectName("menubar")
        Main_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main_Window)
        self.statusbar.setObjectName("statusbar")
        Main_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Main_Window)
        QtCore.QMetaObject.connectSlotsByName(Main_Window)

    def retranslateUi(self, Main_Window):
        _translate = QtCore.QCoreApplication.translate
        Main_Window.setWindowTitle(_translate("Main_Window", "MainWindow"))
        self.dayTable.setText(_translate("Main_Window", "PushButton"))
        self.weekTable.setText(_translate("Main_Window", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_Window = QtWidgets.QMainWindow()
    ui = Ui_Main_Window()
    ui.setupUi(Main_Window)
    Main_Window.show()
    sys.exit(app.exec_())


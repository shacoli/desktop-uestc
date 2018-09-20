# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/shacoli/open-project/desktop-uestc/gui/WeekTable.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WeekTable(object):
    def setupUi(self, WeekTable):
        WeekTable.setObjectName("WeekTable")
        WeekTable.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(WeekTable)
        self.centralwidget.setObjectName("centralwidget")
        self.weektableview = QtWidgets.QTableView(self.centralwidget)
        self.weektableview.setGeometry(QtCore.QRect(170, 130, 256, 192))
        self.weektableview.setObjectName("weektableview")
        WeekTable.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WeekTable)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        WeekTable.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WeekTable)
        self.statusbar.setObjectName("statusbar")
        WeekTable.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(WeekTable)
        QtCore.QMetaObject.connectSlotsByName(WeekTable)

    def retranslateUi(self, WeekTable):
        _translate = QtCore.QCoreApplication.translate
        WeekTable.setWindowTitle(_translate("WeekTable", "MainWindow"))
        self.menu.setTitle(_translate("WeekTable", "文件"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WeekTable = QtWidgets.QMainWindow()
    ui = Ui_WeekTable()
    ui.setupUi(WeekTable)
    WeekTable.show()
    sys.exit(app.exec_())


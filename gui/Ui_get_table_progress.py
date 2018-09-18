# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/shacoli/open-project/desktop-uestc/gui/get_table_progress.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Get_Table_Progress(object):
    def setupUi(self, Get_Table_Progress):
        Get_Table_Progress.setObjectName("Get_Table_Progress")
        Get_Table_Progress.resize(450, 130)
        self.label = QtWidgets.QLabel(Get_Table_Progress)
        self.label.setGeometry(QtCore.QRect(90, 30, 261, 21))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(Get_Table_Progress)
        self.progressBar.setGeometry(QtCore.QRect(80, 70, 301, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Get_Table_Progress)
        QtCore.QMetaObject.connectSlotsByName(Get_Table_Progress)

    def retranslateUi(self, Get_Table_Progress):
        _translate = QtCore.QCoreApplication.translate
        Get_Table_Progress.setWindowTitle(_translate("Get_Table_Progress", "Form"))
        self.label.setText(_translate("Get_Table_Progress", "正在获取课表"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Get_Table_Progress = QtWidgets.QWidget()
    ui = Ui_Get_Table_Progress()
    ui.setupUi(Get_Table_Progress)
    Get_Table_Progress.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\小汇总\eric_project\uestc_pro_1\WeekTable.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WeekTable(object):
    def setupUi(self, WeekTable):
        WeekTable.setObjectName("WeekTable")
        WeekTable.resize(324, 911)
        self.centralwidget = QtWidgets.QWidget(WeekTable)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(30, 80, 271, 731))
        self.scrollArea.setMinimumSize(QtCore.QSize(200, 400))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 252, 1200))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 1200))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.layoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 70, 56, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 80, 31, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_2.setGeometry(QtCore.QRect(70, 60, 131, 71))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 150, 56, 51))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 160, 31, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_3.setGeometry(QtCore.QRect(70, 140, 131, 71))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.layoutWidget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 230, 56, 51))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 240, 31, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_4.setGeometry(QtCore.QRect(70, 220, 131, 71))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.layoutWidget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 310, 56, 51))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 320, 31, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_5.setGeometry(QtCore.QRect(70, 300, 131, 71))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.layoutWidget_5 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 390, 56, 51))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_6.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_6.addWidget(self.label_12)
        self.pushButton_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 400, 31, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_6.setGeometry(QtCore.QRect(70, 380, 131, 71))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.layoutWidget_6 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_6.setGeometry(QtCore.QRect(10, 470, 56, 51))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_7.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_7.addWidget(self.label_14)
        self.pushButton_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setGeometry(QtCore.QRect(210, 480, 31, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_7.setGeometry(QtCore.QRect(70, 460, 131, 71))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.layoutWidget_7 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_7.setGeometry(QtCore.QRect(10, 550, 56, 51))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_7)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_8.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_7)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_8.addWidget(self.label_16)
        self.pushButton_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_8.setGeometry(QtCore.QRect(210, 560, 31, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_8.setGeometry(QtCore.QRect(70, 540, 131, 71))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.layoutWidget_8 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_8.setGeometry(QtCore.QRect(10, 630, 56, 51))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_8)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_9.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_8)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_9.addWidget(self.label_18)
        self.pushButton_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_9.setGeometry(QtCore.QRect(210, 640, 31, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_9.setGeometry(QtCore.QRect(70, 620, 131, 71))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.layoutWidget_9 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_9.setGeometry(QtCore.QRect(10, 710, 56, 51))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_9)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_10.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget_9)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_10.addWidget(self.label_20)
        self.pushButton_10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_10.setGeometry(QtCore.QRect(210, 720, 31, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_10.setGeometry(QtCore.QRect(70, 700, 131, 71))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.layoutWidget_10 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_10.setGeometry(QtCore.QRect(10, 790, 56, 51))
        self.layoutWidget_10.setObjectName("layoutWidget_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget_10)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_21 = QtWidgets.QLabel(self.layoutWidget_10)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_11.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget_10)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_11.addWidget(self.label_22)
        self.pushButton_11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_11.setGeometry(QtCore.QRect(210, 800, 31, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_11.setGeometry(QtCore.QRect(70, 780, 131, 71))
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.layoutWidget_11 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_11.setGeometry(QtCore.QRect(10, 870, 56, 51))
        self.layoutWidget_11.setObjectName("layoutWidget_11")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.layoutWidget_11)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_23 = QtWidgets.QLabel(self.layoutWidget_11)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_12.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget_11)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_12.addWidget(self.label_24)
        self.pushButton_12 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_12.setGeometry(QtCore.QRect(210, 880, 31, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_12.setGeometry(QtCore.QRect(70, 860, 131, 71))
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.layoutWidget_12 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_12.setGeometry(QtCore.QRect(10, 950, 56, 51))
        self.layoutWidget_12.setObjectName("layoutWidget_12")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.layoutWidget_12)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_25 = QtWidgets.QLabel(self.layoutWidget_12)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_13.addWidget(self.label_25)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget_12)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_13.addWidget(self.label_26)
        self.pushButton_13 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_13.setGeometry(QtCore.QRect(210, 960, 31, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_13.setGeometry(QtCore.QRect(70, 940, 131, 71))
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.layoutWidget_13 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_13.setGeometry(QtCore.QRect(10, 1030, 56, 51))
        self.layoutWidget_13.setObjectName("layoutWidget_13")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.layoutWidget_13)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_27 = QtWidgets.QLabel(self.layoutWidget_13)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_14.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget_13)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_14.addWidget(self.label_28)
        self.pushButton_14 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_14.setGeometry(QtCore.QRect(210, 1040, 31, 31))
        self.pushButton_14.setObjectName("pushButton_14")
        self.textBrowser_14 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_14.setGeometry(QtCore.QRect(70, 1020, 131, 71))
        self.textBrowser_14.setObjectName("textBrowser_14")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(11, 99, 54, 21))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(11, 71, 54, 22))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setGeometry(QtCore.QRect(11, 179, 54, 21))
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setGeometry(QtCore.QRect(11, 151, 54, 22))
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(40, 20, 191, 21))
        self.label.setObjectName("label")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_14 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_14.setGeometry(QtCore.QRect(90, 60, 72, 22))
        self.layoutWidget_14.setObjectName("layoutWidget_14")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_14)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_30 = QtWidgets.QLabel(self.layoutWidget_14)
        self.label_30.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_2.addWidget(self.label_30)
        self.spinBox_2 = QtWidgets.QSpinBox(self.layoutWidget_14)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_2.addWidget(self.spinBox_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(160, 60, 72, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_29 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_29.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout.addWidget(self.label_29)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.layoutWidget_15 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_15.setGeometry(QtCore.QRect(230, 60, 72, 22))
        self.layoutWidget_15.setObjectName("layoutWidget_15")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_15)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_31 = QtWidgets.QLabel(self.layoutWidget_15)
        self.label_31.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_3.addWidget(self.label_31)
        self.spinBox_3 = QtWidgets.QSpinBox(self.layoutWidget_15)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_3.addWidget(self.spinBox_3)
        WeekTable.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WeekTable)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 324, 23))
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
        self.pushButton_2.setText(_translate("WeekTable", "+"))
        self.pushButton_3.setText(_translate("WeekTable", "+"))
        self.label_7.setText(_translate("WeekTable", "TextLabel"))
        self.label_8.setText(_translate("WeekTable", "TextLabel"))
        self.pushButton_4.setText(_translate("WeekTable", "+"))
        self.label_9.setText(_translate("WeekTable", "TextLabel"))
        self.label_10.setText(_translate("WeekTable", "TextLabel"))
        self.pushButton_5.setText(_translate("WeekTable", "+"))
        self.label_11.setText(_translate("WeekTable", "TextLabel"))
        self.label_12.setText(_translate("WeekTable", "TextLabel"))
        self.pushButton_6.setText(_translate("WeekTable", "+"))
        self.label_13.setText(_translate("WeekTable", "TextLabel"))
        self.label_14.setText(_translate("WeekTable", "TextLabel"))
        self.pushButton_7.setText(_translate("WeekTable", "+"))
        self.label_15.setText(_translate("WeekTable", "TextLabel"))
        self.label_16.setText(_translate("WeekTable", "TextLabel"))
        self.pushButton_8.setText(_translate("WeekTable", "+"))
        self.label_17.setText(_translate("WeekTable", "TextLabel"))
        self.label_18.setText(_translate("WeekTable", "TextLabel"))
        self.pushButton_9.setText(_translate("WeekTable", "+"))
        self.label_19.setText(_translate("WeekTable", "TextLabel"))
        self.label_20.setText(_translate("WeekTable", "TextLabel"))
        self.pushButton_10.setText(_translate("WeekTable", "+"))
        self.label_21.setText(_translate("WeekTable", "TextLabel"))
        self.label_22.setText(_translate("WeekTable", "TextLabel"))
        self.pushButton_11.setText(_translate("WeekTable", "+"))
        self.label_23.setText(_translate("WeekTable", "TextLabel"))
        self.label_24.setText(_translate("WeekTable", "TextLabel"))
        self.pushButton_12.setText(_translate("WeekTable", "+"))
        self.label_25.setText(_translate("WeekTable", "TextLabel"))
        self.label_26.setText(_translate("WeekTable", "TextLabel"))
        self.pushButton_13.setText(_translate("WeekTable", "+"))
        self.label_27.setText(_translate("WeekTable", "TextLabel"))
        self.label_28.setText(_translate("WeekTable", "TextLabel"))
        self.pushButton_14.setText(_translate("WeekTable", "+"))
        self.label_4.setText(_translate("WeekTable", "TextLabel"))
        self.label_3.setText(_translate("WeekTable", "TextLabel"))
        self.label_6.setText(_translate("WeekTable", "TextLabel"))
        self.label_5.setText(_translate("WeekTable", "TextLabel"))
        self.label.setText(_translate("WeekTable", "您现在查看的是x年x月x日的课表"))
        self.label_30.setText(_translate("WeekTable", "学期"))
        self.label_29.setText(_translate("WeekTable", "周数"))
        self.label_31.setText(_translate("WeekTable", "天数"))
        self.menu.setTitle(_translate("WeekTable", "文件"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WeekTable = QtWidgets.QMainWindow()
    ui = Ui_WeekTable()
    ui.setupUi(WeekTable)
    WeekTable.show()
    sys.exit(app.exec_())


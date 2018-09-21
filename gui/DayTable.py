import sys
import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from Ui_Login import *
from Ui_DayTable import *
sys.path.append("..")
from func import get_table
from config import day_time_config
from data import my_table

class DayTable(QMainWindow,  Ui_DayTable):
    def __init__(self,  parent=None):
        super(DayTable,  self).__init__(parent)
        self.setupUi(self)
        
        self.dateEdit.setDate(QDate.currentDate())
        
        #self.pushButton.mouseDoubleClickEvent(self.pushButton.setText("123"))
        
        self.broadcast_label.setText("")
        self.switch_button.clicked.connect(self.get_day_table)
        self.rescrap_button.clicked.connect(self.get_table_again)
        day = self.dateEdit.date().day()
        month = self.dateEdit.date().month()
        year = self.dateEdit.date().year()

        school_begin_week = datetime.date(2018, 9, 3)
        today_date = datetime.date(year, month, day)
        todays_week = today_date.__sub__(school_begin_week).days % 7 - 1
        todays_day = today_date.__sub__(school_begin_week).days % 7 + 1
        print(todays_week,todays_day)

        ####
        self.label11.setText(day_time_config.time11)  
        self.label12.setText(day_time_config.time12)
        self.label21.setText(day_time_config.time21)
        self.label22.setText(day_time_config.time22)
        self.label31.setText(day_time_config.time31)
        self.label32.setText(day_time_config.time32)
        self.label41.setText(day_time_config.time41)
        self.label42.setText(day_time_config.time42)
        self.label51.setText(day_time_config.time51)
        self.label52.setText(day_time_config.time52)
        self.label61.setText(day_time_config.time61)
        self.label62.setText(day_time_config.time62)
        self.label71.setText(day_time_config.time71)
        self.label72.setText(day_time_config.time72)
        self.label81.setText(day_time_config.time81)
        self.label82.setText(day_time_config.time82)
        self.label91.setText(day_time_config.time91)
        self.label92.setText(day_time_config.time92)
        self.label101.setText(day_time_config.time101)
        self.label102.setText(day_time_config.time102)
        self.label111.setText(day_time_config.time111)
        self.label112.setText(day_time_config.time112)
        self.label121.setText(day_time_config.time121)
        self.label122.setText(day_time_config.time122)
        self.label131.setText(day_time_config.time131)
        self.label132.setText(day_time_config.time132)
        self.label141.setText(day_time_config.time141)
        self.label142.setText(day_time_config.time142)
        self.label151.setText(day_time_config.time151)
        self.label152.setText(day_time_config.time152)
        self.label161.setText(day_time_config.time161)
        self.label162.setText(day_time_config.time162)
        self.label171.setText(day_time_config.time171)
        self.label172.setText(day_time_config.time172)

        textBrowserList = [self.textBrowser_2,self.textBrowser_3,
        self.textBrowser_4,self.textBrowser_5,
        self.textBrowser_7,self.textBrowser_8,
        self.textBrowser_9,self.textBrowser_10,
        self.textBrowser_12,self.textBrowser_13,
        self.textBrowser_14,self.textBrowser_15]
        for i in range(len(textBrowserList)):
            print(todays_day)
            #print(my_table.mytable[i][2])
            if my_table.mytable[i][todays_day-5] == 0:  
                textBrowserList[i].setText("you're free")
            else:
                teachers_name = my_table.mytable[i][todays_day-5][0]
                class_name = my_table.mytable[i][todays_day-5][1]
                class_place = my_table.mytable[i][todays_day-5][2]

                textBrowserList[i].setText("%s\r%s\r%s"%(teachers_name, class_name, class_place))
        ####
    def get_day_table(self):
        #self.scrollAreaWidgetContents.setMinimumHeight(1800)
        pass
    
    def get_table_again(self):
        self.broadcast_label.setText("重新抓取用时为 %1.5f" %float(get_table.write_in_my_table(2017030102012, "402561")))
        self.get_day_table()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = DayTable()
    myWin.show()
    sys.exit(app.exec_())

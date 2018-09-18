import sys
import config
from PyQt5.QtWidgets import *
from Ui_login import *
from Ui_WeekTable import *
from Ui_get_table_progress import *
sys.path.append("..")
from funcs import *

class get_table_progress(QMainWindow,  Ui_Get_Table_Progress):
    def __init__(self,  parent=None):
        super(get_table_progress,  self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ProgressWin = get_table_progress()
    ProgressWin.show()
    sys.exit(app.exec_())

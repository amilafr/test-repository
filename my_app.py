# write the code for main app and first screen
'''import library'''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from instr import *

class MainWin(QWidget):
    # constructor
    def __init__(self):
        super().__init__()

        self.initUI()
        self.next_click()
        self.connects()
        self.set_appear()

        self.show()

    # widget2
    def initUI(self):
        pass

    # next --> ke halaman selanjutnya
    def next_click(self):
        pass

    # button connect ke fungsi
    def connects(self):
        pass

    # bikin window app
    def set_appear(self):
        self.setWindowTitle(txt_title) # judul app
        self.resize(win_width, win_height) # ukuran window (lebar, tinggi)
        self.move(win_x, win_y)

'''bikin window app'''
app = QApplication([])
window = MainWin() # panggil class

app.exec_()
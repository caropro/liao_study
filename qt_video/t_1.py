#coding=utf-8
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle("pyqt_tut1")
window.setGeometry(100,100,400,400)
window.show()

app.exec_()

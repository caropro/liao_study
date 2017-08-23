#coding=utf-8
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class win(QMainWindow):
	def __init__(self):
		super(win, self).__init__()
		self.setGeometry(100,100,400,400)
		self.setWindowTitle("pyqt_tut2")
		self.setWindowIcon(QIcon('favicon.ico'))
		self.show()

app=QApplication(sys.argv)
b=win()
app.exec_()


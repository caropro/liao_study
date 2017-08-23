#coding=utf-8
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class win(QMainWindow):
	def __init__(self):
		super(win, self).__init__()
		self.setWindowIcon(QIcon('favicon.ico'))
		self.setGeometry(100,100,400,400)
		self.home()

	def home(self):
		btn=QPushButton("Quit",self)
		btn.resize(100,100)
		btn.move(100,100)
		btn.clicked.connect(QCoreApplication.instance().quit)
		self.show()

def run():
	app=QApplication(sys.argv)
	b=win()
	app.exec_()

run()
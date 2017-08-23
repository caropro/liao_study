#coding=utf-8
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import urllib
from urllib.request import urlopen

class Form(QDialog):
	def __init__(self,parent=None):
		super(Form, self).__init__(parent)

		self.fromComboBox=QComboBox()
		self.fromComboBox.addItems(['jpg','mov'])
		self.cbutton=QPushButton("check")

		grid = QGridLayout()
		grid.addWidget(self.fromComboBox,1,0)
		grid.addWidget(self.cbutton,1,1)

		self.setLayout(grid)

		self.setWindowTitle("input_type")

		self.fromComboBox.currentIndexChanged.connect(self.check)
		self.cbutton.clicked.connect(self.kick)

	def check(self):
		type=self.fromComboBox.currentText()
		print(type)
	def kick(self):
		s=self.fromComboBox.currentText()
		if s=='jpg':
			print("jpg_hello")
		elif s=='mov':
			print("mov_hello")

app=QApplication(sys.argv)
b=Form()
b.show()
app.exec_()
#coding=utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class test(QDialog):
	def __init__(self,parent=None):
		super(test,self).__init__(parent)

		self.setWindowTitle("test Remove button")

		self.b1=QPushButton("remove b2")
		self.b2=QPushButton("remove b1")

		self.layout=QHBoxLayout()
		self.layout.addWidget(self.b1)
		self.layout.addWidget(self.b2)

		self.setLayout(self.layout)

		self.b1.clicked.connect(self.removeb2)
		self.t=0
	def removeb2(self):
		self.t+=1
		if self.t%2==0:
			self.b2.hide()
		else:
			self.b2.show()

app=QApplication(sys.argv)
b=test()
b.show()
app.exec_()
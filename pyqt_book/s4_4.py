#coding=utf-8
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Form(QDialog):
	def __init__(self,parent=None):
		super(Form, self).__init__(parent)
		self.dial=QDial()
		self.dial.setNotchesVisible(True)
		self.spinBox=QSpinBox()
		buttom=QPushButton('test')

		layout=QHBoxLayout()
		layout.addWidget(self.dial)
		layout.addWidget(self.spinBox)
		layout.addWidget(buttom)

		self.setLayout(layout)
		self.setWindowTitle("signal and slot")

		self.dial.valueChanged.connect(self.spinBox.setValue)
		self.spinBox.valueChanged.connect(self.dial.setValue)
		buttom.clicked.connect(self.dis)
	def dis(self):
		try:
			self.dial.disconnect()
		except:
			print("already stop")
app=QApplication(sys.argv)
b=Form()
b.show()
app.exec_()


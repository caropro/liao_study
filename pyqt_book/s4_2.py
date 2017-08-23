#coding=utf-8
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from math import *

class Form(QDialog):
	def __init__(self,parent=None):
		super(Form,self).__init__(parent)
		self.browser = QTextBrowser()
		self.lineedit = QLineEdit("Type an expression and press Enter")
		self.lineedit.selectAll()
		clear=QPushButton("clean")

		layout = QVBoxLayout()
		layout.addWidget(self.browser)
		layout.addWidget(self.lineedit)
		layout.addWidget(clear)

		self.setLayout(layout)


		self.lineedit.setFocus()
		self.lineedit.returnPressed.connect(self.updateUi)
		clear.clicked.connect(self.cleane)
		self.setWindowTitle("Calculate")

	def updateUi(self):
		try:
			text = str(self.lineedit.text())
			self.browser.append("%s = <b>%s</b>" % (text,eval(text)))
		except:
			self.browser.append("<font color=red>%s is invalid!</font>" % text)
	def cleane(self):
		self.lineedit.clear()

app=QApplication(sys.argv)
b=Form()
b.show()
app.exec_()


app.setQuitOnLastWindowClosed(False)
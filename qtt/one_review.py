#coding=utf-8
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
class prisnt(object):
	def pt(self):
		print("test one")

a=prisnt()
app=QApplication(sys.argv)
b=QPushButton("hello_kitty")
c=QPushButton("a")

b.clicked.connect(app.quit)
c.clicked.connect(a.pt)


layout=QGridLayout()
layout.addWidget(c)
layout.addWidget(b)

wip=QWidget()
wip.setLayout(layout)
wip.show()
app.exec_()
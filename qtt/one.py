#coding=utf-8
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

app=QApplication(sys.argv)
b=QPushButton("hello world")
b.show()
b.clicked.connect(app.quit)
app.exec_()


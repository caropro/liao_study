#coding=utf-8
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time

app=QApplication(sys.argv)

try:
	due = QTime.currentTime()
	message="Alert!"
	if len(sys.argv) <2:
		raise ValueError
	hours,mins=sys.argv[1].split(":")
	due=QTime(int(hours),int(mins))
	if not due.isValid():
		raise ValueError
	if len(sys.argv):
		message = " ".join(sys.argv[2:])
except ValueError:
	message = "Usage: this file"
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/jianxuan/Desktop/test__ui_stFile.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class test(object):
	def __init__(self):
		super(test, self).__init__()


def run():
	app=QtWidgets.QApplication(sys.argv)
	b=test()
	b.show()
	app.exec_()

run()


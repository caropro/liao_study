#coding=utf-8
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
import sys

class win(QtWidgets.QMainWindow):
	def __init__(self):
		super(win, self).__init__()

		self.setWindowIcon(QtGui.QIcon("favicon.png"))
		self.setWindowTitle("Tool bar test")
		self.setGeometry(100,100,400,400)

		extractAct=QtWidgets.QAction("&Open file",self)
		extractAct.setShortcut("Command+g")
		extractAct.setStatusTip("gogogogogogoogog")
		extractAct.triggered.connect(self.close_app)

		self.statusBar()

		menu=self.menuBar()
		filebar=menu.addMenu("File")
		filebar.addAction(extractAct)


		self.home()

	def home(self):
		btn=QtWidgets.QPushButton("Quit",self)
		btn.resize(btn.sizeHint())
		btn.move(50,50)

		extractApp=QtWidgets.QAction(QtGui.QIcon("favicon.png"),"icon test",self)
		extractApp.triggered.connect(self.close_app)

		self.toolBar=self.addToolBar("Quit")
		self.toolBar.addAction(extractApp)


		btn.clicked.connect(self.close_app)
		self.show()

	def close_app(self):
		print("Quit the app")
		#sys.exit()

def run():
	app=QtWidgets.QApplication(sys.argv)
	b=win()
	app.exec_()
run()
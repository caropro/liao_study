#coding=utf-8
from PyQt5 import QtGui
from PyQt5 import QtWidgets
import sys

class win(QtWidgets.QMainWindow):
	def __init__(self):
		super(win, self).__init__()

		self.setWindowTitle("tut_7")
		self.setWindowIcon(QtGui.QIcon('favicon.png'))
		self.setGeometry(100,100,400,400)

		extractAct=QtWidgets.QAction("&Open file",self)
		extractAct.setStatusTip("close the file")
		extractAct.setShortcut("Command+g")
		extractAct.triggered.connect(self.close_app)

		self.statusBar()
		menu=self.menuBar()
		file=menu.addMenu("File")
		file.addAction(extractAct)

		self.home()

	def home(self):
		btn=QtWidgets.QPushButton("Quit",self)
		btn.resize(btn.sizeHint())
		btn.move(100,100)
		btn.clicked.connect(self.close_app)

		extract=QtWidgets.QAction(QtGui.QIcon("favicon.png"),"print",self)
		extract.triggered.connect(self.close_app)

		self.toolbar=self.addToolBar("Quit")
		self.toolbar.addAction(extract)

		self.show()
	def close_app(self):
		choice = QtWidgets.QMessageBox.question( self,"Extract","CLose the app?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
		if choice==QtWidgets.QMessageBox.Yes:
			print("hehehehehhe")
		else:
			pass

def run():
	app=QtWidgets.QApplication(sys.argv)
	b=win()
	app.exec_()

run()
#coding=utf-8
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys

class win(QtWidgets.QMainWindow):
	def __init__(self):
		super(win, self).__init__()

		self.setWindowTitle("tut_8")
		self.setGeometry(100,100,400,500)
		self.setWindowIcon(QtGui.QIcon("favicon.png"))

		extract=QtWidgets.QAction("&File import",self)
		extract.setShortcut("Command+G")
		extract.setStatusTip("print hahaah")
		extract.triggered.connect(self.close_app)

		self.statusTip()

		menu=self.menuBar()
		file=menu.addMenu("File")
		file.addAction(extract)


		self.home()

	def home(self):
		btn=QtWidgets.QPushButton("Quit",self)
		btn.resize(btn.sizeHint())
		btn.move(100,100)
		btn.clicked.connect(self.close_app)

		extract=QtWidgets.QAction(QtGui.QIcon("favicon.png"),"quit_app",self)
		extract.triggered.connect(self.close_app)

		self.toolbar=self.addToolBar("aaa")
		self.toolbar.addAction(extract)

		check=QtWidgets.QCheckBox("enlarge",self)
		check.move(200,200)
		check.toggle()
		check.stateChanged.connect(self.enlarge)
		#默认勾选

		self.show()
	def enlarge(self,state):
		if state== QtCore.Qt.Checked:
			self.setGeometry(50,50,800,800)
		else:
			self.setGeometry(50,50,400,400)

	def close_app(self):
		choice=QtWidgets.QMessageBox.question(self,"!","Really want to Quit?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
		if choice==QtWidgets.QMessageBox.Yes:
			print("hahahahha")
		else:
			pass

def run():
	app=QtWidgets.QApplication(sys.argv)
	b=win()
	app.exec_()

run()
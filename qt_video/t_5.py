#coding=utf-8
from PyQt5 import QtGui
from PyQt5 import  QtCore
from PyQt5 import QtWidgets
import sys

class Win(QtWidgets.QMainWindow):
	def __init__(self):
		super(Win, self).__init__()
		self.setWindowTitle("pyqt_tut5")
		self.setGeometry(50,50,400,500)
		self.setWindowIcon(QtGui.QIcon("favicon.png"))


		extractAction=QtWidgets.QAction("& Find the file",self)
		extractAction.setShortcut("Command+Q")
		extractAction.setStatusTip("import the file path")
		extractAction.triggered.connect(self.closing)
		self.statusBar()
		mainmenu=self.menuBar()
		filmenu=mainmenu.addMenu("&File")
		filmenu.addAction(extractAction)

		self.home()

	def home(self):
		btn=QtWidgets.QPushButton("Quit",self)
		btn.resize(100,100)
		btn.move(50,50)
		btn.clicked.connect(self.closing)

		self.show()
	def closing(self):
		print("hahahah")
		#sys.exit()

def run():
	app=QtWidgets.QApplication(sys.argv)
	b=Win()
	app.exec_()

run()
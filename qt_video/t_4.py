#coding=utf-8
import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore

class win(QtWidgets.QMainWindow):
	def __init__(self):
		super(win, self).__init__()
		self.setWindowIcon(QtGui.QIcon('favicon.png'))
		self.setGeometry(100,100,400,400)
		self.setWindowTitle("pyqt_tut4")

		extractAction=QtWidgets.QAction("&find the file and quit",self)
		extractAction.setShortcut("ctrl+Q")
		extractAction.setStatusTip("save and exit")
		extractAction.triggered.connect(self.closeapp)

		self.statusBar()
		mainMenu=self.menuBar()
		fileMenu=mainMenu.addMenu("&File")
		fileMenu.addAction(extractAction)


		self.home()

	def home(self):
		btn=QtWidgets.QPushButton("Quit",self)
		btn.clicked.connect(self.closeapp)
		btn.resize(200,200)
		btn.move(100,100)
		self.show()
	def closeapp(self):
		print("Waoooooooo")
		self.setWindowTitle("fucn nut")
		#sys.exit()
def run():
	app=QtWidgets.QApplication(sys.argv)
	b=win()
	app.exec_()

run()
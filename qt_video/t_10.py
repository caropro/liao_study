#coding=utf-8
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys

class win(QtWidgets.QMainWindow):
	def __init__(self):
		super(win, self).__init__()

		self.setGeometry(100,100,400,400)
		self.setWindowTitle("tut_10")
		self.setWindowIcon(QtGui.QIcon("favicon.png"))

		extract=QtWidgets.QAction("&close",self)
		extract.setStatusTip("It will close the app")
		extract.setShortcut("Command+G")
		extract.triggered.connect(self.close_app)

		self.statusTip()

		menu=self.menuBar()
		file=menu.addMenu("File")
		file.addAction(extract)
		self.home()

	def home(self):
		btn=QtWidgets.QPushButton("Quit",self)
		btn.resize(btn.sizeHint())
		btn.move(300,300)
		btn.clicked.connect(self.close_app)

		extract=QtWidgets.QAction(QtGui.QIcon("favicon.png"),"quit",self)
		extract.triggered.connect(self.close_app)

		self.toolbar=self.addToolBar("Tone")
		self.toolbar.addAction(extract)

		check=QtWidgets.QCheckBox("relarge",self)
		check.stateChanged.connect(self.relarge)
		check.toggle()
		check.move(130,130)

		self.progress=QtWidgets.QProgressBar(self)
		self.progress.setGeometry(150,100,200,30)

		self.btn=QtWidgets.QPushButton("Download",self)
		self.btn.move(200,140)
		self.btn.clicked.connect(self.download)

		print(self.style().objectName())

		self.stylelabel=QtWidgets.QLabel("macintosh",self)
		self.stylelabel.move(200,70)

		combox=QtWidgets.QComboBox(self)
		combox.addItems(["motif","Windows","cde","macintosh","Fusion","Cleanlooks","windowsvista"])
		combox.move(200,50)

		combox.activated[str].connect(self.stylechange)
		self.show()
	def stylechange(self,text):
		self.stylelabel.setText(text)
		QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create(text))
	def download(self):
		self.precentage=0
		while self.precentage<100:
			self.precentage+=0.001
			self.progress.setValue(self.precentage)
	def relarge(self,state):
		if state==QtCore.Qt.Checked:
			self.setGeometry(100,100,600,600)
		else:
			self.setGeometry(100,100,400,400)
	def close_app(self):
		print("hahahahaahhahaha")

def run():
	app=QtWidgets.QApplication(sys.argv)
	b=win()
	app.exec_()

run()
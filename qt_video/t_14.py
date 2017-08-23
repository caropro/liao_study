#coding=utf-8
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
import sys

class win(QtWidgets.QMainWindow):
	def __init__(self):
		super(win,self).__init__()

		self.setGeometry(100,100,400,400)
		self.setWindowIcon(QtGui.QIcon("favicon.png"))
		self.setWindowTitle("tut_14")

		extract=QtWidgets.QAction("&close",self)
		extract.setStatusTip("close the app")
		extract.setShortcut("Command+G")
		extract.triggered.connect(self.close_app)

		self.statusBar()
		openEditor=QtWidgets.QAction("&Editor",self)
		openEditor.setShortcut("Command+E")
		openEditor.setStatusTip("edit file text")
		openEditor.triggered.connect(self.editor)

		openFile=QtWidgets.QAction("&Open File",self)
		openFile.setStatusTip("open file")
		openFile.setShortcut("Command+O")
		openFile.triggered.connect(self.OpenFile)

		menu=self.menuBar()
		file=menu.addMenu("File")
		file.addAction(extract)
		file.addAction(openFile)

		editorMenu =menu.addMenu("Edit")
		editorMenu.addAction(openEditor)

		self.show()
	def editor(self):
		self.textEdit=QtWidgets.QTextEdit()
		self.setCentralWidget(self.textEdit)
	# def OpenFile(self):
	# 	name=QtWidgets.QFileDialog.getOpenFileName(self,'Open File')
	# 	file = open(name,'r')
	#
	# 	self.editor()
	#
	# 	with file:
	# 		text=file.read()
	# 		self.textEdit.setText(text)

	def OpenFile(self):
		name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
		print(name)
		file = open(name[0], 'r')

		self.editor()

		with file:
			text = file.read()
			self.textEdit.setText(text)
	def close_app(self):
		condition=QtWidgets.QMessageBox.question(self,"???","want to quit?",
												 QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
		if condition==QtWidgets.QMessageBox.Yes:
			print("hehehe")
			sys.exit()
		else:
			pass
def run():
	app=QtWidgets.QApplication(sys.argv)
	b=win()
	app.exec_()

run()
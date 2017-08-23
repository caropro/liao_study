from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys

class win(QtWidgets.QMainWindow):
	def __init__(self):
		super(win, self).__init__()

		self.setGeometry(100,100,400,400)
		self.setWindowTitle("tut_15")
		self.setWindowIcon(QtGui.QIcon("favicon.png"))

		Openfile=QtWidgets.QAction("&Open File",self)
		Openfile.setStatusTip("select and open file")
		Openfile.setShortcut("Command+O")
		Openfile.triggered.connect(self.OpenFile)

		Savefile=QtWidgets.QAction("&Save File",self)
		Savefile.setStatusTip("save file")
		Savefile.setShortcut("Command+O")
		Savefile.triggered.connect(self.SaveFile)

		extract=QtWidgets.QAction("&Close",self)
		extract.setShortcut("Command+Q")
		extract.setStatusTip("Close this App")
		extract.triggered.connect(self.Close_App)

		editor=QtWidgets.QAction("Editor",self)
		editor.triggered.connect(self.Editor)

		self.statusBar()

		menu=self.menuBar()
		File=menu.addMenu("File")
		File.addAction(Openfile)
		File.addAction(Savefile)
		File.addAction(extract)

		File2=menu.addMenu("Edit")
		File2.addAction(editor)

		self.show()

	def OpenFile(self):
		name=QtWidgets.QFileDialog.getOpenFileName(self,"Open File")
		file = open(name[0],"r")

		self.Editor()

		with file:
			text = file.read()
			self.textEdit.setText(text)
	def SaveFile(self):
		name=QtWidgets.QFileDialog.getSaveFileName(self,"Save File")
		file = open(name,"w")
		text=self.textEdit.toPlainText()
		file.write(text)
		file.close()

	def Editor(self):
		self.textEdit=QtWidgets.QTextEdit()
		self.setCentralWidget(self.textEdit)

	def Close_App(self):
		jud=QtWidgets.QMessageBox.question(self,"???","Really want to quit?"
										   ,QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
		if jud==QtWidgets.QMessageBox.Yes:
			sys.exit()

def run():
	app=QtWidgets.QApplication(sys.argv)
	b=win()
	app.exec_()

run()


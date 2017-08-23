#coding=utf-8
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class InputDlg(QDialog):
	def __init__(self,parent=None):
		super(InputDlg, self).__init__(parent)

		label1=QLabel("Name")
		label2=QLabel("Gender")
		label3=QLabel("age")
		label4=QLabel("height")
		label5=QLabel("file_name")

		nb=QPushButton("...")
		fb=QPushButton("...")

		self.nameLabel=QLabel("name")
		self.nameLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)
		self.filelabel=QLabel("filename")
		self.filelabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)

		nb.clicked.connect(self.slotname)
		fb.clicked.connect(self.slotfile)



		layout=QGridLayout()
		layout.addWidget(label1,0,0)
		layout.addWidget(nb,0,1)
		layout.addWidget(self.nameLabel,0,2)
		layout.addWidget(label5,1,0)
		layout.addWidget(fb,1,1)
		layout.addWidget(self.filelabel,1,2)


		self.setLayout(layout)
	def slotname(self):
		name,ok=QInputDialog.getText(self,("title"),("new name"))
		if ok and name:
			self.nameLabel.setText(name)
	def slotfile(self):
		name=QFileDialog.getOpenFileName(self,"Open file Dialog",".","*.py")
		self.filelabel.setText(str(name))



app=QApplication(sys.argv)
f=InputDlg()
f.show()
app.exec_()
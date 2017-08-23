import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class StandardDialog(QDialog):
	def __init__(self,parent=None):
		super(StandardDialog, self).__init__(parent)

		self.setWindowTitle("SrandardDialog")

		filePushbuttom=QPushButton("file_browser")
		colorPushbuttom=QPushButton("color_browser")
		fontPushbuttom=QPushButton("font_broswer")

		self.fileline=QLineEdit("file_name")
		self.colorline=QFrame()
		self.colorline.setFrameShape(QFrame.Box)
		self.colorline.setAutoFillBackground(True)
		self.fontline=QLineEdit("Hi Nut")

		layout=QGridLayout()

		layout.addWidget(filePushbuttom,0,0)
		layout.addWidget(self.fileline,0,1)

		layout.addWidget(colorPushbuttom,1,0)
		layout.addWidget(self.colorline,1,1)

		layout.addWidget(fontPushbuttom,2,0)
		layout.addWidget(self.fontline,2,1)

		self.setLayout(layout)

		filePushbuttom.clicked.connect(self.filework)
		colorPushbuttom.clicked.connect(self.colorwork)
		fontPushbuttom.clicked.connect(self.fontwork)

	def filework(self):
		name=QFileDialog.getOpenFileName(self,"Open file name","/","Python Files(*.py)")
		self.fileline.setText(str(name))
	def colorwork(self):
		color=QColorDialog.getColor(Qt.blue)
		if color.isValid():
			self.colorline.setPalette(QPalette(color))
	def fontwork(self):
		font,ok=QFontDialog.getFont()
		if ok:
			self.fontline.setFont(font)

app=QApplication(sys.argv)
q=StandardDialog()
q.show()
app.exec_()

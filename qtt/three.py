#coding=utf-8
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

class Geometry(QDialog):
	def __init__(self,parent=None):
		super(Geometry,self).__init__(parent)

		self.setWindowTitle("Geometry")

		Label1=QLabel("x0:")
		Label2=QLabel("y0:")
		Label3=QLabel("frameGeometry():")
		Label4=QLabel("pos():")
		Label5=QLabel("geometry():")
		Label6=QLabel("width():")
		Label7=QLabel("height():")
		Label8=QLabel("rect():")
		Label9=QLabel("size():")

		self.xLabel=QLabel()
		self.yLabel=QLabel()
		self.frameGeoLabel=QLabel()
		self.posLabel=QLabel()
		self.geoLabel=QLabel()
		self.widthLabel=QLabel()
		self.heightLabel=QLabel()
		self.rectLabel=QLabel()
		self.sizeLabel=QLabel()

		layout=QGridLayout()
		layout.addWidget(Label1,0,0)
		layout.addWidget(self.xLabel,0,1)
		layout.addWidget(Label2,1,0)
		layout.addWidget(self.yLabel,1,1)
		layout.addWidget(Label3,2,0)
		layout.addWidget(self.frameGeoLabel,2,1)
		layout.addWidget(Label4,3,0)
		layout.addWidget(self.posLabel,3,1)
		layout.addWidget(Label5,4,0)
		layout.addWidget(self.geoLabel,4,1)
		layout.addWidget(Label6,5,0)
		layout.addWidget(self.widthLabel,5,1)
		layout.addWidget(Label7,6,0)
		layout.addWidget(self.heightLabel,6,1)
		layout.addWidget(Label8,7,0)
		layout.addWidget(self.rectLabel,7,1)
		layout.addWidget(Label9,8,0)
		layout.addWidget(self.sizeLabel,8,1)

		self.setLayout(layout)

		self.updateLabel()

	def moveEvent(self, event):
		self.updateLabel()

	def resizeEvent(self, event):
		self.updateLabel()

	def updateLabel(self):
		temp=str

		self.xLabel.setText(temp(self.x()))
		self.yLabel.setText(temp(self.y()))
		self.frameGeoLabel.setText(temp(self.frameGeometry().x())+','+
								   temp(self.frameGeometry().y())+","+
								   temp(self.frameGeometry().width())+','+
								   temp(self.frameGeometry().height()))
		self.posLabel.setText(temp(self.pos().x())+','+
							  temp(self.pos().y()))
		self.geoLabel.setText(temp(self.geometry().x())+','+
							  temp(self.geometry().y())+','+
							  temp(self.geometry().width())+','+
							  temp(self.geometry().height()))
		self.widthLabel.setText(temp(self.width()))
		self.heightLabel.setText(temp(self.height()))
		self.rectLabel.setText(temp(self.rect().x())+","+
							   temp(self.rect().y())+","+
							   temp(self.rect().width())+","+
							   temp(self.rect().height()))
		self.sizeLabel.setText(temp(self.size().width())+","+
							   temp(self.size().height()))

app=QApplication(sys.argv)
form=Geometry()
form.show()
app.exec_()

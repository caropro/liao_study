#coding=utf-8
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import urllib
from urllib.request import urlopen

class Form(QDialog):
	def __init__(self,parent=None):
		super(Form, self).__init__(parent)
		date=self.getdata()
		rates=sorted(self.rates.keys())

		dateLabel=QLabel(date)
		self.fromComboBox=QComboBox()
		self.fromComboBox.addItems(rates)

		self.fromSpinBox=QDoubleSpinBox()
		self.fromSpinBox.setRange(0.01,10000000)
		self.fromSpinBox.setValue(1.00)

		self.toComboBox=QComboBox()
		self.toComboBox.addItems(rates)
		self.toLabel = QLabel("1.00")

		grid = QGridLayout()
		grid.addWidget(dateLabel,0,0)
		grid.addWidget(self.fromComboBox,1,0)
		grid.addWidget(self.fromSpinBox,1,1)
		grid.addWidget(self.toComboBox,2,0)
		grid.addWidget(self.toLabel,2,1)

		self.setLayout(grid)

		self.fromComboBox.currentIndexChanged.connect(self.updateUi)
		self.toComboBox.currentIndexChanged.connect(self.updateUi)
		self.fromSpinBox.valueChanged.connect(self.updateUi)

		self.setWindowTitle("Currency")

	def updateUi(self):
		to =str(self.toComboBox.currentText())
		from_=str(self.fromComboBox.currentText())
		amount=(self.rates[from_]/self.rates[to])*self.fromSpinBox.value()
		self.toLabel.setText("%0.2f" % amount)

	def getdata(self):
		self.rates={}
		try:
			date = "Unknow"
			fh = urllib.request.urlopen("http://www.bankofcanada.ca/valet/observations/group/FX_RATES_DAILY/csv")
			name = []
			ratedic = {}
			finalrate = []
			date = ''
			for line in fh:
				l = str(line).strip()[2:-4]
				if l.startswith("FX"):
					l = l.split(",")
					name.append(l[0])
					ratedic[l[0]] = l[1] + l[2]
				elif l.startswith("ERROR"):
					break
				elif l.startswith("2017"):
					finalrate.append(l)

			finalrate = finalrate[-1].split(",")
			date = finalrate.pop(0)
			for r, n in zip(finalrate, name):
				self.rates[n] = float(r)
			#
			# for line in fh:
			# 	if not line or line.startswith(("#","Closing")):
			# 		continue
			# 	fields=line.split(",")
			# 	if line.startswith('Date'):
			# 		date=fields[-1]
			# 	else:
			# 		try:
			# 			value = float(fields[-1])
			# 			self.rates[fields[0]]=value
			# 		except ValueError:
			# 			pass
			# return "Exchange Rates Date: " +date
		except Exception as e:
			return "Failed to download:\n%s" % e


app=QApplication(sys.argv)
b=Form()
b.show()
app.exec_()
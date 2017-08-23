#coding=utf-8
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
import sys


class NumberFormatDlg(QtWidgets.QDialog):
	x = pyqtSignal()
	def __init__(self,format,parent=None):
		super(NumberFormatDlg, self).__init__(parent)
		self.format= dict(thousandsseparator=',', decimalmarker='.', decimalplaces=2, rednegatives=False)

		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		punctuationRe=QtCore.QRegExp(r"[ ;:.,]")

		thousandLabel=QtWidgets.QLabel("&Thousands separator")
		self.thousandsEdit=QtWidgets.QLineEdit(format["thousandsseparator"])
		thousandLabel.setBuddy(self.thousandsEdit)
		self.thousandsEdit.setMaxLength(1)
		self.thousandsEdit.setValidator(QtGui.QRegExpValidator(punctuationRe,self))

		decimalMarkerLabel=QtWidgets.QLabel("Decimal &marker")
		self.decimalMarkerEdit=QtWidgets.QLineEdit(format["decimalmarker"])
		decimalMarkerLabel.setBuddy(self.decimalMarkerEdit)
		self.decimalMarkerEdit.setMaxLength(1)
		self.decimalMarkerEdit.setValidator(QtGui.QRegExpValidator(punctuationRe,self))
		self.decimalMarkerEdit.setInputMask("X")

		decimalPlacesLabel=QtWidgets.QLabel("&Dicimal places")
		self.decimalPlacesSpinBox=QtWidgets.QSpinBox()
		decimalPlacesLabel.setBuddy(self.decimalMarkerEdit)
		self.decimalPlacesSpinBox.setRange(0,6)
		self.decimalPlacesSpinBox.setValue(format["decimalplaces"])

		self.redNegativeCheckBox=QtWidgets.QCheckBox("&Red negative number")
		self.redNegativeCheckBox.setChecked(format["rednegatives"])

		buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Cancel)

		grid=QtWidgets.QGridLayout()
		grid.addWidget(thousandLabel,0,0)
		grid.addWidget(self.thousandsEdit,0,1)
		grid.addWidget(decimalMarkerLabel,1,0)
		grid.addWidget(self.decimalMarkerEdit,1,1)
		grid.addWidget(decimalPlacesLabel,2,0)
		grid.addWidget(self.decimalPlacesSpinBox,2,1)
		grid.addWidget(self.redNegativeCheckBox,3,0,1,2)
		grid.addWidget(buttonBox,4,0,1,2)
		self.setLayout(grid)

		buttonBox.accepted.connect(self.accept)
		buttonBox.rejected.connect(self.reject)

		self.setWindowTitle("Set Number Format (Modal)")


	def accept(self):
		class ThousandsError(Exception):pass
		class DecimalError(Exception):pass
		Punctuation = frozenset(" ,;:.")

		thousands=self.thousandsEdit.text()
		decimal=self.decimalMarkerEdit.text()

		try:
			if len(decimal)==0:
				raise  DecimalError("The decimal marker may not be empty")
			if len(thousands)>1:
				raise  ThousandsError("The thousands separator may only be empty or one character.")
			if len(decimal)>1:
				raise DecimalError("The decimal marker must be one character")
			if thousands==decimal:
				raise ThousandsError("The thousands seperator and the decimal marker must be different")
			if thousands and thousands not in Punctuation:
				raise ThousandsError("The thousands seperator must be a punctuation symbol")
			if decimal not in Punctuation:
				raise DecimalError("The decimal marker must be a punctuation symbol")
		except ThousandsError as e:
			QtWidgets.QMessageBox.warning(self,"Thousands Separator Error,e")
			self.thousandsEdit.selectAll()
			self.thousandsEdit.setFocus()

		except DecimalError as e:
			QtWidgets.QMessageBox.warning(self,"Decimal Marker Error",e)
			self.decimalMarkerEdit.selectAll()
			self.decimalMarkerEdit.setFocus()
			return

		self.format["thousandsseperator"]=thousands
		self.format["decimalmarker"]=decimal
		self.format["decimalplaces"]=self.decimalPlacesSpinBox.value()
		self.format["rednegatives"]=self.redNegativeCheckBox.isChecked()

		self.x.connect(self.pr)
		self.x.emit()
	def pr(self):
		print("ahhahahahaha")



def run():
	app=QtWidgets.QApplication(sys.argv)

	formats=dict(thousandsseparator=',',decimalmarker='.',decimalplaces=2,rednegatives=False)
	b=NumberFormatDlg(formats)
	b.show()
	app.exec_()

run()
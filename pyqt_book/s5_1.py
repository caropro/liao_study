#coding=utf-8
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
import sys
class PenPropertiesDlg(QtWidgets.QDialog):
	def __init__(self,parent=None):
		super(PenPropertiesDlg, self).__init__(parent)


		widthLabel=QtWidgets.QLabel("&Width:")
		self.widthSpinBox=QtWidgets.QSpinBox()
		widthLabel.setBuddy(self.widthSpinBox)
		self.widthSpinBox.setAlignment((QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter))
		self.widthSpinBox.setRange(0,24)

		self.beveledCheckBox=QtWidgets.QCheckBox("&Beveled edges")
		styleLabel=QtWidgets.QLabel("Style:")
		self.styleComboBox=QtWidgets.QComboBox()
		self.styleComboBox.addItems(["Solid","Dashed","Dotted","DashDotted","DashDotDotted"])
		okButton=QtWidgets.QPushButton("&OK")
		cancelButton=QtWidgets.QPushButton("Cancel")


		buttonLayer=QtWidgets.QHBoxLayout()
		buttonLayer.addStretch()
		buttonLayer.addWidget(okButton)
		buttonLayer.addWidget(cancelButton)

		layout=QtWidgets.QGridLayout()
		layout.addWidget(widthLabel,0,0)
		layout.addWidget(self.widthSpinBox,0,1)
		layout.addWidget(self.beveledCheckBox,0,2)
		layout.addWidget(styleLabel,1,0)
		layout.addWidget(self.styleComboBox,1,1,1,2)
		layout.addLayout(buttonLayer,2,0,1,3)

		self.setLayout(layout)

		okButton.clicked.connect(self.accept)
		cancelButton.clicked.connect(self.reject)

		self.setWindowTitle("Pen Properties")



def run():
	app=QtWidgets.QApplication(sys.argv)
	b=PenPropertiesDlg()
	b.show()
	app.exec_()

run()
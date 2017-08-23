#coding=utf-8
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class MessageBoxDialog(QDialog):
	def __init__(self,parent=None):
		super(MessageBoxDialog, self).__init__(parent)
		self.setWindowTitle("MessageBox")
		self.label=QLabel("About Qt MessageBox")
		questionButton=QPushButton("Question")
		informationButton=QPushButton("Information")
		warningButton=QPushButton("Warning")
		criticalButton=QPushButton("Critical")
		aboutButton=QPushButton("About")
		aboutqtButton=QPushButton("About Qt")
		customButton=QPushButton("Custom")

		gridLayout=QGridLayout(self)

		gridLayout.addWidget(self.label,0,0,1,2)
		gridLayout.addWidget(questionButton,1,0)
		gridLayout.addWidget(informationButton,1,1)
		gridLayout.addWidget(warningButton,2,0)
		gridLayout.addWidget(criticalButton,2,1)
		gridLayout.addWidget(aboutButton,3,0)
		gridLayout.addWidget(aboutqtButton,3,1)
		gridLayout.addWidget(customButton,4,0)

		questionButton.clicked.connect(self.slotQuestion)
		informationButton.clicked.connect(self.slotInformation)
		warningButton.clicked.connect(self.slotWarning)
		criticalButton.clicked.connect(self.slotCritical)
		aboutButton.clicked.connect(self.slotAbout)
		aboutqtButton.clicked.connect(self.slotAboutQt)
		customButton.clicked.connect(self.slotCustom)

	def slotQuestion(self):
		button=QMessageBox.question(self,"Question",
									self.tr("已到达文档结尾，是否从头查找?"),
									QMessageBox.Ok|QMessageBox.Cancel,
									QMessageBox.Ok)
		if button==QMessageBox.Ok:
			self.label.setText("Qusetion button/Ok")
		elif button==QMessageBox.Cancel:
			self.label.setText("Qusetion button/Cancel")
		else:
			return

	def slotInformation(self):
		QMessageBox.information(self,"Information",
								self.tr("填写任意想告诉用户的信息!"))
		self.label.setText("information Messagebox")
	def slotWarning(self):
		button=QMessageBox.warning(self,"Warning",
								   self.tr("是否保存对文档的修改?"),
								   QMessageBox.Save|QMessageBox.Discard|QMessageBox.Cancel,
								   QMessageBox.Save)
		if button==QMessageBox.Save:
			self.label.setText("Warning button/Save")
		elif button==QMessageBox.Discard:
			self.label.setText("Warning button/Discard")
		elif button==QMessageBox.Cancel:
			self.label.setText("Warning button/Cancel")
		else:
			return

	def slotCritical(self):
		QMessageBox.critical(self,"Critical",
							 self.tr("提醒用户一个致命错误!"))
		self.label.setText("Critical Message")
	def slotAbout(self):
		QMessageBox.about(self,"About",self.tr("About 事例"))
		self.label.setText("About MessageBox")

	def slotAboutQt(self):
		QMessageBox.aboutQt(self,"About Qt")
		self.label.setText("About Qt MesageBox")

	def slotCustom(self):
		customMsgBox=QMessageBox(self)
		customMsgBox.setWindowTitle("Custom message box")
		lockButton=customMsgBox.addButton(self.tr("lock"),
									  QMessageBox.ActionRole)
		unlockButton=customMsgBox.addButton(self.tr("unlock"),
										QMessageBox.ActionRole)
		cancelButton=customMsgBox.addButton("cancel",QMessageBox.ActionRole)

		customMsgBox.setText(self.tr("This is Custom MessageBox!"))
		customMsgBox.exec_()

		button=customMsgBox.clickedButton()
		if button==lockButton:
			self.label.setText("Custom MessageBox/Lock")
		elif button==unlockButton:
			self.label.setText("Custom MessageBox/Unlock")
		elif button==cancelButton:
			self.label.setText("Custom MessageBox/Cancel")

app=QApplication(sys.argv)
MessageBox=MessageBoxDialog()
MessageBox.show()
app.exec_()
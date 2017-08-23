#coding=utf-8
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class fruit(QListWidget):
	def __init__(self):
		super(fruit, self).__init__()
		add_btn=QPushButton("&Add")
		edit_btn=QPushButton("Edit")
		remove_btn=QPushButton("Remove")
		btn=QPushButton("Sort")
		up_btn=QPushButton("Up")
		close_btn=QPushButton("Close")

		self.listtab=QListWidget(self)

		self.listtab.addItems(["a","b","c","dd","ae","asff"])

		layout=QHBoxLayout()
		layoutb=QVBoxLayout()

		layoutb.addWidget(add_btn)
		layoutb.addWidget(edit_btn)
		layoutb.addWidget(remove_btn)
		layoutb.addWidget(btn)
		layoutb.addWidget(up_btn)
		layoutb.addWidget(close_btn)

		layout.addWidget(self.listtab)
		layout.addLayout(layoutb)

		self.setLayout(layout)

		add_btn.clicked.connect(self.adds)
		edit_btn.clicked.connect(self.edits)
		remove_btn.clicked.connect(self.removes)
		up_btn.clicked.connect(self.up)
		btn.clicked.connect(self.sortlist)
		close_btn.clicked.connect(self.close_app)
		self.show()

	def adds(self):
		s,ok=QInputDialog.getText(self,"get name and import","fruit name")
		self.listtab.addItem(str(s))

	def edits(self):
		row = self.listtab.currentRow()
		item = self.listtab.item(row)
		if item is not None:
			title = "Edit %s" % "Name"
			string, ok = QInputDialog.getText(self, title, title,
											  QLineEdit.Normal, item.text())
			if ok and string:
				item.setText(string)
	def removes(self):
		row=self.listtab.currentRow()
		item=self.listtab.item(row)
		if QMessageBox.question(self, "Remove","Remove`%s'?" % item.text(),QMessageBox.Yes|QMessageBox.No):
			self.listtab.takeItem(row)

	def up(self):
		row = self.listtab.currentRow()
		if row >= 1:
			item = self.listtab.takeItem(row)
			self.listtab.insertItem(row- 1, item)
			self.listtab.setCurrentItem(item)
	def sortlist(self):
		self.listtab.sortItems()

	def close_app(self):
		sys.exit()

def run():
	app=QApplication(sys.argv)
	b=fruit()
	app.exec_()

run()
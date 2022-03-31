from PyQt5.QtWidgets import QComboBox, QMainWindow, QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
import sys


class MainWindow(QMainWindow):

	def __init__(self):
		super().__init__()

		combobox1 = QComboBox() #Graphene_percentage 0.    0.005 0.01  0.02  0.03
		combobox1.addItem(0)
		combobox1.addItem(0.005)
		combobox1.addItem(0.01)
		combobox1.addItem(0.02)
		combobox1.addItem(0.03)

		combobox2 = QComboBox()
		combobox2.addItems(['One', 'Two', 'Three', 'Four'])

		layout = QVBoxLayout()
		layout.addWidget(combobox1)
		layout.addWidget(combobox2)

		container = QWidget()
		container.setLayout(layout)

		self.setCentralWidget(container)

	def current_text_changed(self, s):
		print("Current text: ", s)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QColor, QBrush

class App(QWidget):
	
	def __init__(self):
		super().__init__()
		self.left = 0
		self.top = 0
		self.width = 1920
		self.height = 1080
		self.initUI()

	def initUI(self):
		print('init')
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.label = QLabel(self)
		self.loadImage('./slides/default.jpg')

		self.showFullScreen()

	def loadImage(self,img):
		pixmap = QPixmap(img)
		pixmap = pixmap.scaled(self.width,self.height)
		pixmap = self.addLabel(pixmap)
		self.label.setPixmap(pixmap)

	def updateScreen(self,img):
		self.loadImage(img)

	def addLabel(self,image):
		print('addlabel')

		painter = QPainter()

		painter.begin(image)
		painter.setBrush(QBrush(QColor(200,0,151)))
		painter.drawRect(0,0,1920,200)
		painter.end()


		return image
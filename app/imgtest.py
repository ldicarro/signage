import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainScreen(QMainWindow):
	def __init__(self,parent=None):
		QMainWindow.__init__(self,parent)
		self.left = 0
		self.top = 0
		self.width = 640
		self.height = 480
		self.initUI()

	def initUI(self):
		print('init')
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.label = LabelWidget(self)
		self.setCentralWidget(self.label)

	def changeImage(self):
		print('changeImage')
		self.label.updateImage()

class LabelWidget(QWidget):
	def __init__(self, parent):
		super().__init__(parent)
		self.layout = QVBoxLayout(self)

		self.label = QLabel()
		self.addImage()
		self.layout.addWidget(self.label)
		self.currentImage = QImage()

		self.animation = QVariantAnimation()
		self.animation.valueChanged.connect(self.changeColor)

	def addImage(self):
		image = QImage()
		image.load('./slides/default.jpg')
		image = image.convertToFormat(QImage.Format_ARGB32)

		image2 = self.setOpacity(image,1.0)
		self.currentImage = image2
		self.label.setGeometry(0,0,640,480)
		self.label.setPixmap(QPixmap.fromImage(image2))

	def setOpacity(self,image,opacity):
		newImage = QImage(640, 480,QImage.Format_ARGB32)
		newImage.fill(Qt.transparent)
		
		painter = QPainter(newImage)
		painter.setOpacity(opacity)
		painter.drawImage(QRect(0, 0,640, 480), image)

		return newImage

	def updateImage(self):
		self.doFadeOut()
		loop = QEventLoop()
		self.animation.finished.connect(loop.quit)
		loop.exec_()
		'''
		image = QImage()
		image.load('./slides/PDFPSmT.jpg')
		
		self.label.setPixmap(QPixmap.fromImage(image))
		'''
	
	def changeColor(self, color):
		palette = self.palette()
		palette.setColor(QPalette.WindowText, color)
		self.setPalette(palette)

	def doFadeOut(self):
		print('doFadeOut')
		self.animation.stop()
		self.animation.setStartValue(QColor(0,0,0,255))
		self.animation.setEndValue(QColor(0,0,0,0))
		self.animation.setDuration(2000)
		self.animation.setEasingCurve(QEasingCurve.OutBack)
		self.animation.start()
		
		



if __name__ == "__main__":
	app = QApplication(sys.argv)

	mainscr = MainScreen()
	mainscr.show()

	timer = QTimer()
	timer.singleShot(2000,mainscr.changeImage)
	
	sys.exit(app.exec_())

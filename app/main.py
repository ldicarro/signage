import sys
import json
from slide import Slide
from app import App
import sched, time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


duration = 2.0
slides = []
listPosition = 0

def init():
	with open('config.json','r') as f:
		jdata = json.load(f)

	slideData = jdata['slides']

	for slide in slideData:
		print(slide['file'])
		temp = Slide(slide)
		slides.append(temp)


def slideShow():
	global listPosition
	ex.updateScreen(slides[listPosition].file)
	listPosition += 1

	if listPosition >= len(slides):
		listPosition = 0

###########################################

if __name__ == '__main__':
	init()

	app = QApplication(sys.argv)
	ex = App()

	timer = QTimer()
	timer.timeout.connect(slideShow)
	timer.start(duration * 1000)
	
	sys.exit(app.exec_())


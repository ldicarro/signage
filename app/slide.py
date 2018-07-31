from PIL import Image

class Slide():

	def __init__(self,json):
		self.id = json['id']
		self.name = json['name']
		self.start = json['start']
		self.end = json['end']
		self.file = json['file']
		self.getImage()

	def getImage(self):
		self.im = Image.open(self.file)
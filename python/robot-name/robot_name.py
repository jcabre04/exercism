import datetime
import random

class Robot:
	def __init__(self):
		random.seed()
		self.build_name()
		print(self.name)

	def build_name(self):
		now = datetime.datetime.now()
		name0 = now.strftime("%a")[0].upper()
		name1 = now.strftime("%b")[0].upper()
		name2 = str(random.randint(0, 999)).zfill(3)
		self.name = name0 + name1 + name2

	def reset(self):
		random.seed()
		self.build_name()
		print(self.name)
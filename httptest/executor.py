# executor.py
# Copyright (c) 2021 Alessio Rubicini
# This code is licensed under MIT license (see LICENSE for details)

import json

class Executor(object):

	def __init__(self):
		self.name = ""
		self.author = ""
		self.description = ""
		self.requests = {}

	def parseJsonConfig(self, filePath):
		
		with open(filePath, "r") as file:
			
			config = json.load(file.read())

			self.requests = dict(config)


	def runRequests(self):
		pass

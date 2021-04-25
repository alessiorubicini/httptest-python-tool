# executor.py
# Copyright (c) 2021 Alessio Rubicini
# This code is licensed under MIT license (see LICENSE for details)

import json
import requests as r

# This object is responsible of executing the HTTP requests
# using the options passed from the Parser
class Executor(object):

	def __init__(self, options):
		self.info = {}
		self.requests = []
		self.options = options

		self.parseJsonConfig()

	def parseJsonConfig(self):
		
		# Open JSON config file
		# The file path is specified in Parser's options
		with open(self.options.config, "r") as file:
			
			# Read test configuration from JSON file
			config = json.load(file)

			self.info = dict(config["package"])
			self.requests = config["requests"]


	def runRequests(self):
		if len(self.requests) == 0:
			print("No requests to be executed")
			return

		# Creates the output file if it doesn't exists
		with open(self.options.output, 'w+') as fp:
			pass
		
		# Test HTTP requests writing output to output file
		with open(self.options.output, "a") as outputFile:
			success = 0
			failed = 0

			l = len(self.requests)
			i = 0
			self.printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
			for req in self.requests:
				

				# Send HTTP request
				httpreq = r.request(req["method"], url=req["url"], params=(req["body"] if req["method"] == "POST" else {}), headers=req["headers"])

				self.printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

				# Check the result
				if httpreq.status_code == req["expected-status"]:
					success += 1
				else:
					failed += 1

				# Write result to output file
				outputFile.write(req["title"] + " - Status code: " + str(httpreq.status_code) + " - Response: " + httpreq.content.decode('utf-8') + "\n\n")

				i += 1

			# Print final result on terminal
			print(f"HTTP requests tested ✓\n\033[92m{success} succeed\033[92m | \033[91m{failed} failed\n\033[95mCheck {self.options.output} file for details")


	def printProgressBar(self, iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
		"""
		Call in a loop to create terminal progress bar
		@params:
			iteration   - Required  : current iteration (Int)
			total       - Required  : total iterations (Int)
			prefix      - Optional  : prefix string (Str)
			suffix      - Optional  : suffix string (Str)
			decimals    - Optional  : positive number of decimals in percent complete (Int)
			length      - Optional  : character length of bar (Int)
			fill        - Optional  : bar fill character (Str)
			printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
		"""
		percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
		filledLength = int(length * iteration // total)
		bar = fill * filledLength + '-' * (length - filledLength)
		print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
		# Print New Line on Complete
		if iteration == total: 
			print()


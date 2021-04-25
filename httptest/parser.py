# parser.py
# Copyright (c) 2021 Alessio Rubicini
# This code is licensed under MIT license (see LICENSE for details)

import optparse
import sys
import os

# This object is responsible of parsing user option 
class Parser(optparse.OptionParser):
	
	def __init__(self):
		super().__init__("usage: httptest <command> arg1 arg2")
		self.setupCommands()

	def setupCommands(self):
		self.add_option('-c', '--config', action="store", default="httptest.json", type="string", help="specify the configuration file (httptest.json by default)")
		self.add_option('-o', '--output', action="store", default="httpoutput.txt", type="string", help="specify the output file (httpresult.txt by default)")

	def getOptions(self):
		(options, args) = self.parse_args()

		# Check if config file exists
		if not os.path.isfile(options.config):
			print(f"\033[93mWarning: configuration JSON file '{options.config}' does not exists. Type httptest init to create it.\033[93m")
			exit()

		# Check if output directory exists
		if not os.path.isdir(os.path.dirname(options.output)):
			print(f"\033[93mWarning: output directory '{os.path.dirname(options.output)}' does not exists \033[93m")
			exit()

		return options

	# Display errors for unknown options
	def error(self, msg):
		print(f"Unknonw option: {sys.argv[1]}")




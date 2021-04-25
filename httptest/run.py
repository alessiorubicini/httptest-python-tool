#!/usr/bin/env python3
# run.py
# Copyright (c) 2021 Alessio Rubicini
# This code is licensed under MIT license (see LICENSE for details)

import optparse
import sys

from parser import Parser
from executor import Executor

parser = Parser()
executor = Executor(parser.getOptions())

# Help message
if "-h" in sys.argv or "--help" in sys.argv:
	parser.print_help()


# Run requests
if "run" in sys.argv:
	executor.runRequests()

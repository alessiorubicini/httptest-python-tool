# run.py
# Copyright (c) 2021 Alessio Rubicini
# This code is licensed under MIT license (see LICENSE for details)

import optparse
from executor import Executor

if __name__ == "__main__":

	parser = optparse.OptionParser("usage: httptest [options] arg1 arg2")

	parser.add_option("-S", "--sequential", default="", type="string")

	
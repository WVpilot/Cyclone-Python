#import sys
import argparse
from planner import Planner

class Cyclone:
	def __init__(self):
		self.parser = argparse.ArgumentParser(description="This is a Python port for Cyclone for easier access for SHC")
		self.add_arguments()

	def add_arguments(self):
		self.parser.add_argument("-o", "--output", help="Defines the path for the output file of an operation")
		self.parser.add_argument("-v", "--verbose", help="Verbose output", action="store_true")
		self.parser.add_argument("--plan", help="Create a .gcode file from an input mesh", action="store_true")
		self.parser.add_argument("-i", "--input", help="Input .wind file")

	def parse_args(self):
		self.args = self.parser.parse_args()
	
	def run(self):
		if self.args.verbose:
			self.verbose = True
		if self.args.input & self.args.output:
			planner = Planner(self.args.input, self.args.output)
			planner.run()

#Handle argument inputs
if __name__ == "__main__":
	cyclone = Cyclone()
	cyclone.parse_args()
	cyclone.run()
	pass
#import sys
import argparse

class Cyclone:
	def __init__(self):
		self.parser = argparse.ArgumentParser(description="This is a Python port for Cyclone for easier access for SHC")
		self.add_arguments(self)

	def add_arguments(self):
		self.parser.add_argument("-o", help="Defines the path for the output file of an operation")
		self.parser.add_argument("-v", help="Verbose output")
		self.parser.add_argument("--plan", help="Create a .gcode file from an input mesh")
		self.parser.add_argument("input", help="Input .wind file")

	def parse_args(self):
		self.args = self.parser.parse_args()
	
	def run(self):
		if self.args.verbose:
			self.verbose = True
		

#Handle argument inputs


if __name__ == "__main__":
	cyclone = Cyclone()
	cyclone.parse_args()

	pass
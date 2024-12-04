import json

class Planner:
	def __init__(self, input, output):
		self.inputPath = input
		self.outputPath = output

	def run(self):
		with open(input) as f:
			data = json.load(f)
		data
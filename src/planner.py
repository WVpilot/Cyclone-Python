import json
import numpy

class Planner:
	def __init__(self, input, output):
		self.inputPath = input
		self.outputPath = output
		self.gcode = ''

	def move(self, x = None, y = None, z = None):
		self.gcode += 'G1 '
		if (x != None):
			self.gcode += f'X{x} '
		if (y != None):
			self.gcode += f'Y{y} '
		if (z != None):
			self.gcode += f'Z{z}'
		self.gcode += '\n'

	def run(self):
		#Load the input file
		with open(self.inputPath) as f:
			data = json.load(f)
		
		feedRate = data['defaultFeedRate']

		self.x = 0
		self.y = 0
		self.z = 0

		#Set positioning to relative and the set position to absolute 0
		self.gcode += f'G91\n'
		self.gcode += f'G92 X{self.x} Y{self.y} Z{self.z}\n'
		
		#Set feed rate
		self.gcode += f'G1 F{feedRate}\n'

		#Iterate through each layer set
		for layer in data['layers']:
			match layer['windType']:
				case 'helical':
					

					if layer['terminal']:
						break
					pass
				case 'hoop':
					
					self.headAngle = 90 - numpy.rad2deg(numpy.atan(data['mandrelParameters']['diameter'] / data['towParameters']['width']))
					#Lock out the wind layer to secure it, either use input setting or default of one rotation
					self.y += layer['lockDegrees'] if (layer['lockDegrees'] != 'undefined') else 360
					self.move(y = self.y)

					#Calculate movements for the wind
					self.rotations = numpy.max(numpy.abs(data['mandrelParameters']['windLength'] / data['towParameters']['width']))
					self.y += self.rotations * 360
					self.x += data['mandrelParameters']['windLength']
					self.move(x = self.x, y = self.y)
					
					#Lock the far end of the layer
					self.y += layer['lockDegrees'] if (layer['lockDegrees'] != 'undefined') else 360
					self.move(y = self.y)

					if layer['terminal']:
						print("Terminal layer encountered, ending wind planning")
					else:
						self.y += self.rotations * 360
						self.x -= data['mandrelParameters']['windLength']
						self.move(x = self.x, y = self.y)
					
		#Write gcode to file, create a new file is current file does not exist
		try:
			print("Writing gcode to output file")
			with open(self.outputPath, "w") as g:
				g.write(self.gcode)
		except:
			print("Warning: ouput file does not exist, creating a new file using output path")
			with open(self.outputPath, "x") as g:
				g.write(self.gcode)

'''
A script which measures the time a user rests the mouse on the target before clicking
'''

import os, sys
import json
import numpy as np
import csv

rootdir = './CSVSeparated/'

checkNum = 0

fileHandles = {}
count = 0
filenum = 0
lastName=None
initialTime = 0
clickTime = 0
hoverTime = 0

hovertimesinlab = []
hovertimesoutlab = []

'''
CSV FORMAT

Anthony Coleman	1.42021E+12	137	375	mouseDown
[      0             1       2   3     4]
      Name			time 	 y   x    type
'''

for current_directory, directories, files in os.walk(rootdir):
	
	for file in files:
		filenum += 1
		filepath = os.path.join(current_directory,file)
	

		with open(filepath) as infile:
			parsed = csv.reader(infile)

			for row in parsed:
		
				name = parsed[0]

				if(checkNum == 1 and parsed[0] == initialTime):
					clickTime = float(parsed[0])
					hoverTime = initialTime - clickTime
					checkNum = 0
				
				if(parsed[4] == "mouseDown"):
					checkNum = 1
					initialTime = float(parsed[1])
					hoverTime = 0
					clickTime = 0

				if(hoverTime != 0):
					print hoverTime

				hoverTime = 0
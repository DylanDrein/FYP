'''
A script which measures the time a user rests the mouse on the target before clicking
'''

import os
from operator import itemgetter, attrgetter, methodcaller
import json

rootdir ='./UsersReversed/clarence-roberts-reversed.json'

checkNum = 0

fileHandles = {}
count = 0
filenum = 0
lastName=None
initialTime = 0
clickTime = 0
hoverTime = 0

#for current_directory, directories, files in os.walk(rootdir):
	
	#for file in files:
		
	#	filenum += 1
	#	filepath = os.path.join(current_directory,file)

		#with open(filepath) as infile:
with open(rootdir) as infile:

	for line in infile:
	
		parsed = json.loads(line)
		
		name = parsed['name']

		if(checkNum == 1):
			clickTime = parsed['time']
			hoverTime = initialTime - clickTime
			checkNum = 0
		
		if(parsed['type'] == "mouseDown"):
			checkNum = 1
			initialTime = parsed['time']
			hoverTime = 0
			clickTime = 0

		if(hoverTime != 0):
			print hoverTime

		hoverTime = 0
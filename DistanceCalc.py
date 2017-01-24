'''
A script which measures the distance a users mouse travels from the initial point
to the target mouse click, and compares it to the ideal time.

declare actualglobaldistance var
declare eucliddistance var
declare vars for coords of start point
declare var for time of start point

comes down, reaches MouseDown
saves the current mouse coord in var1
goes to the next
gets the distance between current and var1
adds it to actualglobaldistance
current becomes var1
repeat...

if mouseup: use coords of var1 and start point to get
	linear euclidean distance

compare actualglobaldistance with this

compare current time with start time and
	get actual vs ideal speed



'''

import os
from operator import itemgetter, attrgetter, methodcaller
import json
import numpy as np

rootdir ='./UsersReversed/test-user.json'

actualDist = 0
optimalDist = 0
startPoint = 0
prevPoint = 0
startTime = 0
goalTime = 0
measuring = False
velocities = []
prevTime = 0

def dist(a, b):
	return np.linalg.norm(a-b)

#for current_directory, directories, files in os.walk(rootdir):
	
	#for file in files:
		
	#	filenum += 1
	#	filepath = os.path.join(current_directory,file)

		#with open(filepath) as infile:
with open(rootdir) as infile:

	for line in infile:
	
		parsed = json.loads(line)

		if(parsed['type'] == "mouseDown"):
			measuring = True
			startPoint = np.array((parsed['x'], parsed['y']))
			prevPoint = np.array((parsed['x'], parsed['y']))
			startTime = parsed['time']
			prevTime = parsed['time']

		if((parsed['time'] < (startTime - 2000) or parsed['type'] == "mouseUp") and measuring):
			measuring = False
			print "Actual distance: " + str(actualDist)
			actualDist = 0
			print "Average actual speed: " + str(np.mean(velocities)) + "px/ms"
			optimalDist = dist(prevPoint, startPoint)
			timeTaken = startTime - prevTime
			print "Time taken: " + str(timeTaken) + "ms"
			print "Optimal Distance: " + str(optimalDist) + "\n"
			optimalDist = 0

		if(measuring == True):
			currentPos = np.array((parsed['x'], parsed['y']))
			currentTime = parsed['time']
			localTime = prevTime - currentTime
			localDist = dist(prevPoint, currentPos)
			actualDist = actualDist + localDist

			if(localTime != 0):
				localVel = (localDist/localTime)
				velocities.append(localVel)



		prevPoint = np.array((parsed['x'], parsed['y']))
		prevTime = parsed['time']
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
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.tools as tls
tls.set_credentials_file(username='DylanDrein', api_key='ysXKN96SeJ6a6lM1WMKs')


rootdir ='./UsersReversed/test-user.json'

actualDist = 0
optimalDist = 0
startPoint = 0
prevPoint = 0
startTime = 0
goalTime = 0
measuring = False
prevTime = 0
velocities = []
optOverAct = []


def dist(a, b):
	return np.linalg.norm(a-b)

#for current_directory, directories, files in os.walk(rootdir):
	
	#for file in files:
		
	#	filenum += 1
	#	filepath = os.path.join(current_directory,file)

		#with open(filepath) as infile:
with open(rootdir) as infile:
	parsed = ""
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
			optimalDist = dist(prevPoint, startPoint)
			timeTaken = startTime - prevTime
			optOverAct.append(optimalDist/actualDist)
			print "Actual distance: " + str(actualDist)
			print "Average actual speed: " + str(np.mean(velocities)) + "px/ms"
			print "Time taken: " + str(timeTaken) + "ms"
			print "Optimal Distance: " + str(optimalDist) + "\n"
			optimalDist = 0
			actualDist = 0

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

	if(measuring == True):
		print "Actual distance: " + str(actualDist)
		print "Average actual speed: " + str(np.mean(velocities)) + "px/ms"
		optimalDist = dist(prevPoint, startPoint)
		timeTaken = startTime - prevTime
		print "Time taken: " + str(timeTaken) + "ms"
		print "Optimal Distance: " + str(optimalDist) + "\n"

	plotLen = len(optOverAct)
	plotRange = range(plotLen)
	print "plotlen " + str(plotLen)
	print "plotrange " + str(plotRange)
	print optOverAct
	width = 1
	plt.bar(plotRange, optOverAct, width, color="blue")
	plt.ylabel("Efficiency (Optimal length/Actual length)")
	plt.xlabel("")
	plt.show()
	#fig = plt.gcf()
	#plot_url = py.plot_mpl(fig, filename='mpl-basic-bar')


'''
create histogram comparing efficiency of paths taken
optimal / actual

'''
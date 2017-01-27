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
from matplotlib.lines import Line2D
import plotly.plotly as py


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

#histogram array
optOverAct = []

#dot plot array
actualVals = []
optimalVals = []


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

			#histogram
			optOverAct.append(optimalDist/actualDist)

			#dot plot
			actualVals.append(actualDist)
			optimalVals.append(optimalDist)

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
		optimalDist = dist(prevPoint, startPoint)
		timeTaken = startTime - prevTime

		#histogram
		optOverAct.append(optimalDist/actualDist)

		#dot plot
		actualVals.append(actualDist)
		optimalVals.append(optimalDist)

		print "Actual distance: " + str(actualDist)
		print "Average actual speed: " + str(np.mean(velocities)) + "px/ms"
		print "Time taken: " + str(timeTaken) + "ms"
		print "Optimal Distance: " + str(optimalDist) + "\n"

	#DOT PLOT
	maxVals = [max(optimalVals), max(actualVals)]
	plt.plot(actualVals, optimalVals, 'ro', label='Efficiency')
	x = max(maxVals)
	#y = max(maxVals)
	#plt.plot([0,0], [1400, 1400], 'k-')
	plt.plot([0, x], [0, x], 'k-', label='Efficiency')
	#l = Line2D([0, max(actualVals)], [0, max(optimalVals)])
	plt.title("Graph of Efficiency (Optimal/Actual)")
	plt.ylabel("Optimal Mouse Path Lengths")
	plt.xlabel("Actual Mouse Path Lengths")
	plt.axis([0, max(actualVals) + 100, 0, max(optimalVals) + 100])
	for a, b in enumerate(optOverAct):
		plt.annotate(b, (actualVals[a], optimalVals[a]))

	plt.show()



''' #HISTOGRAM

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

'''
create histogram comparing efficiency of paths taken
optimal / actual

'''
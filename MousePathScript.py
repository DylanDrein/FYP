import os, sys
import json
import numpy as np
import matplotlib.pyplot as plt

rootdir = './UsersReversed/'
	
actualDist = 0
optimalDist = 0
startPoint = []
startTime = 0
prevPoint = []
prevTime = 0
measuring = False
#velocities = []

filenum = 0
graphindex = 0

optOverAct = []
actualVals = []
optimalVals = []
velocities = []
xvalues = []
yvalues = []

#actualnum = 0
#optimalnum = 0

filename = ""

def dist(a, b):
	return np.linalg.norm(a-b)

for current_directory, directories, files in os.walk(rootdir):
	
	for file in files:
		filenum += 1
		filepath = os.path.join(current_directory,file)
		
		with open(filepath) as infile:
			parsed = ""
			for line in infile:
				
				parsed = json.loads(line)

				filename = parsed['name'].lower().replace(" ", "-")

				if(parsed['type'] == "mouseDown"):
					measuring = True
					startPoint = np.array((parsed['x'], parsed['y']))
					prevPoint = np.array((parsed['x'], parsed['y']))
					startTime = parsed['time']
					prevTime = parsed['time']
					xvalues.append(parsed['x'])
					yvalues.append(parsed['y'])

				if((parsed['time'] < (startTime - 1500) or parsed['type'] == "mouseUp") and measuring):
					measuring = False
					optimalDist = dist(prevPoint, startPoint)
					timeTaken = startTime - prevTime

					#histogram
					if(actualDist != 0):
						optOverAct.append(optimalDist/actualDist)
					
					#dot plot
					actualVals.append(actualDist)
					#actualnum = actualnum + 1
					optimalVals.append(optimalDist)
					#optimalnum = optimalnum + 1


					#PLOT MOUSE PATHS (THERES GONNA BE A LOT..)
					if not os.path.exists("./MousePlots/" + filename):
					    try:
					        os.makedirs("./MousePlots/" + filename)
					        print "created"
					    except OSError as exc: # Guard against race condition
					        if exc.errno != errno.EEXIST:
					            raise

					plt.plot(xvalues, yvalues, 'r.')
					plt.plot(startPoint[0], startPoint[1], 'b*')
					plt.title("$Mouse$ $Path$")
					plt.xlabel("$x-coordinates$")
					plt.ylabel("$y-coordinates$")
					plt.axis([0, max(xvalues) + 100, 0, max(yvalues) + 100])
					plt.savefig("./MousePlots/" + filename + '/' + str(graphindex) + '.png')
					plt.clf()
					graphindex += 1
					del xvalues[:]
					del yvalues[:]

					#print "Actual distance: " + str(actualDist)
					#print "Average actual speed: " + str(np.mean(velocities)) + "px/ms"
					#print "Time taken: " + str(timeTaken) + "ms"
					#print "Optimal Distance: " + str(optimalDist) + "\n"
					optimalDist = 0
					actualDist = 0

				if(measuring == True):
					currentPos = np.array((parsed['x'], parsed['y']))
					currentTime = parsed['time']
					localTime = prevTime - currentTime
					localDist = dist(prevPoint, currentPos)
					actualDist = actualDist + localDist

					xvalues.append(parsed['x'])
					yvalues.append(parsed['y'])

					if(localTime != 0):
						localVel = (localDist/localTime)
						velocities.append(localVel)

				prevPoint = np.array((parsed['x'], parsed['y']))
				prevTime = parsed['time']
				
			if(measuring == True):
				optimalDist = dist(prevPoint, startPoint)
				#timeTaken = startTime - prevTime
				xvalues.append(parsed['x'])
				yvalues.append(parsed['y'])

				#histogram
				if(actualDist != 0):
					optOverAct.append(optimalDist/actualDist)
					

				#dot plot
				actualVals.append(actualDist)
				#actualnum = actualnum + 1
				optimalVals.append(optimalDist)
				#optimalnum = optimalnum + 1
				optimalDist = 0
				actualDist = 0
				'''
				print "Actual distance: " + str(actualDist)
				print "Average actual speed: " + str(np.mean(velocities)) + "px/ms"
				print "Time taken: " + str(timeTaken) + "ms"
				print "Optimal Distance: " + str(optimalDist) + "\n"
				print filenum
				print actualnum
				print optimalnum
				'''

			graphindex = 0
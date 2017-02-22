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

times = []

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
					times.append(startTime)

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

					if(localTime != 0):
						localVel = (localDist/localTime)
						velocities.append(localVel)

				prevPoint = np.array((parsed['x'], parsed['y']))
				prevTime = parsed['time']
				
			if(measuring == True):
				optimalDist = dist(prevPoint, startPoint)
				#timeTaken = startTime - prevTime

				#histogram
				if(actualDist != 0):
					optOverAct.append(optimalDist/actualDist)

				#dot plot
				actualVals.append(actualDist)
				#actualnum = actualnum + 1
				optimalVals.append(optimalDist)
				#optimalnum = optimalnum + 1
				times.append(startTime)
				
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

		
		times = np.array(times)
		#print len(times)

		times = (times/max(times)).astype(np.float)
		print len(times)
		print len(optimalVals)
		print len(actualVals)

		'''
		#DOT PLOT (WORKS!!)
		maxVals = [max(optimalVals), max(actualVals)]
		plt.scatter(actualVals, optimalVals, c=times, cmap=plt.cm.winter)
		x = max(maxVals)
		plt.plot([0, x], [0, x], 'k-')
		plt.title("$Graph$ $of$ $Efficiency$ $(Optimal/Actual)$")
		plt.ylabel("$Optimal$ $Mouse$ $Path$ $Lengths$ $(px)$")
		plt.xlabel("$Actual$ $Mouse$ $Path$ $Lengths$ $(px)$")
		plt.axis([0, max(actualVals) + 100, 0, max(optimalVals) + 100])
		plt.savefig('./ScatterPlots2/' + filename + '.png')
		plt.clf()
		'''
		del actualVals[:]
		del optimalVals[:]
		del optOverAct[:]

		times = []
		del times[:]
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
import json
import numpy as np
import matplotlib.pyplot as plt

rootdir = './UsersReversed/'
#rootdir = './ActualVsOptimalCalculator/'
	
actualDist = 0
optimalDist = 0
startPoint = 0
startTime = 0
prevPoint = 0
prevTime = 0
measuring = False
#velocities = []

filenum = 0

optOverAct = []
actualVals = []
optimalVals = []

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

				if((parsed['time'] < (startTime - 2000) or parsed['type'] == "mouseUp") and measuring):
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

					#if(localTime != 0):
					#	localVel = (localDist/localTime)
					#	velocities.append(localVel)

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
				optimalDist = 0
				actualDist = 0
				#print "Actual distance: " + str(actualDist)
				#print "Average actual speed: " + str(np.mean(velocities)) + "px/ms"
				#print "Time taken: " + str(timeTaken) + "ms"
				#print "Optimal Distance: " + str(optimalDist) + "\n"
				#print filenum
				#print actualnum
				#print optimalnum

			
			
			#data = [actualVals, optimalVals, optOverAct]
			#np.savetxt("./ActualOptimal2/" + filename + ".csv", data, fmt='%1.6f', delimiter=",")
			#print filenum

			del actualVals[:]
			del optimalVals[:]
			del optOverAct[:]
			

			#DOT PLOT (WORKS!!!)
			maxVals = [max(optimalVals), max(actualVals)]
			plt.plot(actualVals, optimalVals, 'r.')
			x = max(maxVals)
			plt.plot([0, x], [0, x], 'k-')
			plt.legend(loc='upper right')
			plt.title("$Graph$ $of$ $Efficiency$ $(Optimal/Actual)$")
			plt.ylabel("$Optimal$ $Mouse$ $Path$ $Lengths$")
			plt.xlabel("$Actual$ $Mouse$ $Path$ $Lengths$")
			plt.axis([0, max(actualVals) + 100, 0, max(optimalVals) + 100])
			#for a, b in enumerate(optOverAct):
			#	plt.annotate(b, (actualVals[a], optimalVals[a]))

			plt.show()
			plt.clf()
			print filenum


			del actualVals[:]
			del optimalVals[:]
			del optOverAct[:]

			
			
			plt.savefig('./ScatterPlots/' + filename + '.png')
			plt.clf()



			#HISTOGRAM (WORKS!!)
			plt.hist(optOverAct, 200, normed = 1, facecolor='green', alpha = 1)
			plt.title("$Histogram$ $of$ $Optimal/Actual$ $path$ $lengths$")
			plt.xlabel("$Value$")
			plt.ylabel("$Frequency$")
			plt.legend(loc='upper right')
			plt.show()
			plt.clf()

			del actualVals[:]
			del optimalVals[:]
			del optOverAct[:]
			
			'''



			#BOXPLOT
			data = [actualVals, optimalVals]
			labels = ["Actual", "Optimal"]
			plt.xticks([actualVals],['Actual', 'Optimal'])
			plt.boxplot(data, labels = labels, showfliers = True)
			plt.ylabel('Optimal/Actual path length')
			plt.xlabel('Actual vs. Optimal paths')
			plt.show()
			print filenum
			plt.clf()

			del actualVals[:]
			del optimalVals[:]
			
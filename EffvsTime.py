import os, sys
import json
import numpy as np
import matplotlib.pyplot as plt
import csv
'''
CSV FORMAT

Anthony Coleman	1.42021E+12	137	375	mouseDown
[      0             1       2   3     4]
      Name			time 	 y   x    type
'''


rootdir = './CSVSeparated/'
	
actualDist = 0
optimalDist = 0
startPoint = []
startTime = 0
prevPoint = []
prevTime = 0
measuring = False

filenum = 0
graphindex = 0

efficiency1 = []
actualVals1 = []
optimalVals1 = []

efficiency2 = []
actualVals2 = []
optimalVals2 = []

times1 = []
times2 = []

hourmilliseconds = 3600000

firstlabmidnight = 1415318400000 # 7th of november
lab1start = 1415358000000 # 11am
lab1end = 1415365200000 # 1pm

secondlabmidnight = 1417132800000 # 28th of november
lab2start = 1417172400000 # 11am
lab2end = 1417179600000 # 1pm

filename = ""

def dist(a, b):
	return np.linalg.norm(a-b)

for current_directory, directories, files in os.walk(rootdir):
	
	for file in files:
		filenum += 1
		filepath = os.path.join(current_directory,file)
		
		with open(filepath) as infile:
			parsed = csv.reader(infile)
			for row in parsed:

				filename = row[0].lower().replace(" ", "-")


				# LAB ONE
				if(int(row[1]) > lab1start and int(row[1]) < lab1end):
					if(row[4] == "mouseDown"):
						measuring = True
						startPoint = np.array((int(row[3]), int(row[2])))
						prevPoint = np.array((int(row[3]), int(row[2])))
						startTime = int(row[1])
						prevTime = int(row[1])
						

					if((int(row[1]) < (startTime - 1500) or row[4] == "mouseUp") and measuring):
						measuring = False
						optimalDist = dist(prevPoint, startPoint)

						#histogram
						if(actualDist != 0):
							efficiency1.append(optimalDist/actualDist)
						
							#dot plot
							actualVals1.append(actualDist)
							#actualnum = actualnum + 1
							optimalVals1.append(optimalDist)
							#optimalnum = optimalnum + 1
							times1.append(startTime)

						#print "Actual distance: " + str(actualDist)
						#print "Average actual speed: " + str(np.mean(velocities)) + "px/ms"
						#print "Time taken: " + str(timeTaken) + "ms"
						#print "Optimal Distance: " + str(optimalDist) + "\n"
						optimalDist = 0
						actualDist = 0

					if(measuring == True):
						currentPos = np.array((int(row[3]), int(row[2])))
						currentTime = int(row[1])
						localDist = dist(prevPoint, currentPos)
						actualDist = actualDist + localDist


					prevPoint = np.array((int(row[3]), int(row[2])))
					prevTime = int(row[1])

				# LAB TWO
				if(int(row[1]) > lab2start and int(row[1]) < lab2end):
					if(row[4] == "mouseDown"):
						measuring = True
						startPoint = np.array((int(row[3]), int(row[2])))
						prevPoint = np.array((int(row[3]), int(row[2])))
						startTime = int(row[1])
						prevTime = int(row[1])
						

					if((int(row[1]) < (startTime - 1500) or row[4] == "mouseUp") and measuring):
						measuring = False
						optimalDist = dist(prevPoint, startPoint)

						#histogram
						if(actualDist != 0):
							efficiency2.append(optimalDist/actualDist)
						
							#dot plot
							actualVals2.append(actualDist)
							#actualnum = actualnum + 1
							optimalVals2.append(optimalDist)
							#optimalnum = optimalnum + 1
							times2.append(startTime)

						#print "Actual distance: " + str(actualDist)
						#print "Average actual speed: " + str(np.mean(velocities)) + "px/ms"
						#print "Time taken: " + str(timeTaken) + "ms"
						#print "Optimal Distance: " + str(optimalDist) + "\n"
						optimalDist = 0
						actualDist = 0

					if(measuring == True):
						currentPos = np.array((int(row[3]), int(row[2])))
						currentTime = int(row[1])
						localDist = dist(prevPoint, currentPos)
						actualDist = actualDist + localDist


					prevPoint = np.array((int(row[3]), int(row[2])))
					prevTime = int(row[1])
				
			if(int(row[1]) > lab1start and int(row[1]) < lab1end):
				if(measuring == True):
					optimalDist = dist(prevPoint, startPoint)
					#timeTaken = startTime - prevTime

					#histogram
					if(actualDist != 0):
						efficiency1.append(optimalDist/actualDist)

						#dot plot
						actualVals1.append(actualDist)
						#actualnum = actualnum + 1
						optimalVals1.append(optimalDist)
						#optimalnum = optimalnum + 1
						times1.append(startTime)

					optimalDist = 0
					actualDist = 0

			if(int(row[1]) > lab2start and int(row[1]) < lab2end):
				if(measuring == True):
					optimalDist = dist(prevPoint, startPoint)
					#timeTaken = startTime - prevTime

					#histogram
					if(actualDist != 0):
						efficiency2.append(optimalDist/actualDist)

						#dot plot
						actualVals2.append(actualDist)
						#actualnum = actualnum + 1
						optimalVals2.append(optimalDist)
						#optimalnum = optimalnum + 1
						times2.append(startTime)

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
		
		times1 = np.array(times1)
		times2 = np.array(times2)

		

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
		

		print len(times1)
		print len(times2)
		print len(efficiency1)
		print len(efficiency2)
		'''
		
		plt.title("Graph of efficiency over time")
		f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
		ax1.scatter(times1, efficiency1)
		ax2.scatter(times2, efficiency2)
		ax1.set_title("Lab 1: 11:00-13:00 7/11/14")
		ax2.set_title("Lab 2: 11:00-13:00 28/11/14")
		plt.show()
		plt.clf()
		

		del actualVals1[:]
		del optimalVals1[:]
		del efficiency1[:]
		del actualVals2[:]
		del optimalVals2[:]
		del efficiency2[:]

		times1 = []
		times2 = []
		del times1[:]
		del times2[:]
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

totaltimes1 = []
totaltimes2 = []
totalefficiency1 = []
totalefficiency2 = []

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
		measuring = False

		with open(filepath) as infile:
			parsed = csv.reader(infile)

			for row in parsed:

				filename = row[0].lower().replace(" ", "-")

				# LAB ONE
				if((float(row[1]) > lab1start) and (float(row[1]) < lab1end)):
					if(row[4] == "mouseDown"):
						measuring = True
						startPoint = np.array((float(row[3]), float(row[2])))
						prevPoint = np.array((float(row[3]), float(row[2])))
						startTime = float(row[1])
						prevTime = float(row[1])
						
					if((float(row[1]) < (startTime - 1500) or row[4] == "mouseUp") and measuring):
						measuring = False
						optimalDist = dist(prevPoint, startPoint)

						#histogram
						if(actualDist != 0):
							efficiency1.append(optimalDist/actualDist)
						
							actualVals1.append(actualDist)
							
							optimalVals1.append(optimalDist)
							
							times1.append(startTime)

						#print "Actual distance: " + str(actualDist)
						#print "Average actual speed: " + str(np.mean(velocities)) + "px/ms"
						#print "Time taken: " + str(timeTaken) + "ms"
						#print "Optimal Distance: " + str(optimalDist) + "\n"
						optimalDist = 0
						actualDist = 0
						startTime = 0

					if(measuring == True):
						currentPos = np.array((float(row[3]), float(row[2])))
						currentTime = float(row[1])
						localDist = dist(prevPoint, currentPos)
						actualDist = actualDist + localDist


					prevPoint = np.array((float(row[3]), float(row[2])))
					prevTime = float(row[1])

				if(float(row[1]) > lab1end and float(row[1]) < lab2start):
					measuring = False

				# LAB TWO
				if((float(row[1]) > lab2start) and (float(row[1]) < lab2end)):
					if(row[4] == "mouseDown"):
						measuring = True
						startPoint = np.array((float(row[3]), float(row[2])))
						prevPoint = np.array((float(row[3]), float(row[2])))
						startTime = float(row[1])
						prevTime = float(row[1])
						

					if((float(row[1]) < (startTime - 1500) or row[4] == "mouseUp") and measuring):
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
						startTime = 0

					if(measuring == True):
						currentPos = np.array((float(row[3]), float(row[2])))
						currentTime = float(row[1])
						localDist = dist(prevPoint, currentPos)
						actualDist = actualDist + localDist


					prevPoint = np.array((float(row[3]), float(row[2])))
					prevTime = float(row[1])
			
			
			if(measuring == True):	
				if((float(row[1]) > lab1start) and (float(row[1]) < lab1end)):
					optimalDist = dist(prevPoint, startPoint)

					if(actualDist != 0):
						efficiency1.append(optimalDist/actualDist)

						actualVals1.append(actualDist)
						
						optimalVals1.append(optimalDist)
						
						times1.append(startTime)

					optimalDist = 0
					actualDist = 0
					startTime = 0

				if((float(row[1]) > lab2start) and (float(row[1]) < lab2end)):
					optimalDist = dist(prevPoint, startPoint)
					
					if(actualDist != 0):
						efficiency2.append(optimalDist/actualDist)

						actualVals2.append(actualDist)
						
						optimalVals2.append(optimalDist)
						
						times2.append(startTime)

					optimalDist = 0
					actualDist = 0
					startTime = 0
				measuring = False

		totalefficiency1.append(efficiency1)
		totalefficiency2.append(efficiency2)
		totaltimes1.append(times1)
		totaltimes2.append(times2)
		


		'''
		times1 = np.array(times1)
		times2 = np.array(times2)

		m1, b1 = np.polyfit(times1, efficiency1, 1)
		m2, b2 = np.polyfit(times2, efficiency2, 1)
	
		f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
		#.title("Graph of efficiency over time")
		ax1.set_title("Lab 1: 11:00-13:00 7/11/14")
		ax1.scatter(times1, efficiency1)
		ax1.plot(times1, m1*times1 + b1, '-')
		ax2.set_title("Lab 2: 11:00-13:00 28/11/14")
		ax2.scatter(times2, efficiency2)
		ax2.plot(times2, m2*times2 + b2, '-')
		plt.xticks(rotation = 'vertical')
		plt.subplots_adjust(bottom=0.2)
		plt.savefig('./ScatterPlots2/' + filename + '.png')
		plt.clf()
		'''
		

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

		print filenum

m1, b1 = np.polyfit(totaltimes1, totalefficiency1, 1)
m2, b2 = np.polyfit(totaltimes2, totalefficiency2, 1)

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
#.title("Graph of efficiency over time")
ax1.set_title("Lab 1: 11:00-13:00 7/11/14")
ax1.scatter(totaltimes1, totalefficiency1)
ax1.plot(totaltimes1, m1*totaltimes1 + b1, '-')
ax2.set_title("Lab 2: 11:00-13:00 28/11/14")
ax2.scatter(totaltimes2, totalefficiency2)
ax2.plot(totaltimes2, m2*totaltimes2 + b2, '-')
plt.xticks(rotation = 'vertical')
plt.subplots_adjust(bottom=0.2)
plt.savefig('./ScatterPlots2/' + "xtotallabs" + '.png')
plt.clf()
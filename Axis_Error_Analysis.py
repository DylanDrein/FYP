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

inlabXactual = []
inlabXoptimal = []
inlabYactual = []
inlabYoptimal = []
outlabXactual = []
outlabXoptimal = []
outlabYactual = []
outlabYoptimal = []

lab1start = 1415358000000 # 11am 7th november
lab1end = 1415365200000 # 1pm

lab2start = 1417172400000 # 11am 28th of november
lab2end = 1417179600000 # 1pm

filename = ""

handle1 = open("./Metricstest/inlabxactual.csv", 'wb')
handle2 = open("./Metricstest/inlabxoptimal.csv", 'wb')
handle3 = open("./Metricstest/inlabyactual.csv", 'wb')
handle4 = open("./Metricstest/inlabyoptimal.csv", 'wb')
handle5 = open("./Metricstest/outlabxactual.csv", 'wb')
handle6 = open("./Metricstest/outlabxoptimal.csv", 'wb')
handle7 = open("./Metricstest/outlabyactual.csv", 'wb')
handle8 = open("./Metricstest/outlabyoptimal.csv", 'wb')

inlabactx = 0
inlabacty = 0
outlabactx = 0
outlabacty = 0


def dist(a, b):
	return float(np.linalg.norm(a-b))

for current_directory, directories, files in os.walk(rootdir):
	
	for file in files:
		filenum += 1
		filepath = os.path.join(current_directory,file)

		#optimalDist = 0
		actualDist = 0
		startTime = 0
		prevTime = 0
		measuring = False
		inlabactx = 0
		inlabacty = 0
		outlabactx = 0
		outlabacty = 0

		with open(filepath) as infile:
			parsed = csv.reader(infile)

			for row in parsed:

				filename = row[0].lower().replace(" ", "-")

				# IN LAB
				if( ((float(row[1]) > lab1start) and (float(row[1]) < lab1end)) or ((float(row[1]) > lab2start) and (float(row[1]) < lab2end)) ):
					if(row[4] == "mouseDown"):					
						measuring = True
						startPoint = np.array((float(row[3]), float(row[2])))
						prevPoint = np.array((float(row[3]), float(row[2])))
						startTime = float(row[1])
						prevTime = float(row[1])
						
					if((float(row[1]) < (startTime - 1450) or row[4] == "mouseUp") and measuring):
						measuring = False

						#histogram
						if(actualDist != 0 and (float(optimalDist/actualDist) != float(1.0)) and (startTime - prevTime >= float(0.0))):
							inlabXoptimal.append(dist(np.array(prevPoint[0], 0), np.array(startPoint[0], 0))) #inlaboptimalDistX
							inlabYoptimal.append(dist(np.array(0, prevPoint[1]), np.array(0, startPoint[1]))) #inlaboptimalDistX
							inlabXactual.append(inlabactx)
							inlabYactual.append(inlabacty)

						optimalDist = 0
						actualDist = 0
						startTime = 0
						prevTime = 0
						inlabactx = 0
						inlabacty = 0

					if(measuring == True):
						currentPos = np.array((float(row[3]), float(row[2])))
						localDistX = dist(np.array(prevPoint[0], 0), np.array(currentPos[0], 0))
						localDistY = dist(np.array(0, prevPoint[1]), np.array(0, currentpos[1]))
						inlabactX = float(inlabactX + localDistX)
						inlabactY = float(inlabactY + localDistY)

					prevPoint = np.array((float(row[3]), float(row[2])))
					prevTime = float(row[1])
					
				# OUT OF LAB
				else:
					if(row[4] == "mouseDown"):
						measuring = True
						startPoint = np.array((float(row[3]), float(row[2])))
						prevPoint = np.array((float(row[3]), float(row[2])))
						startTime = float(row[1])
						prevTime = float(row[1])
						
					if((float(row[1]) < (startTime - 1450) or row[4] == "mouseUp") and measuring):
						measuring = False
						optimalDist = float(dist(prevPoint, startPoint))

						#histogram
						if(actualDist != 0 and (float(optimalDist/actualDist) != float(1.0)) and (startTime - prevTime >= float(0.0))):
							outlabXoptimal.append(dist(np.array(prevPoint[0], 0), np.array(startPoint[0], 0))) #outlaboptimalDistX
							outlabYoptimal.append(dist(np.array(0, prevPoint[1]), np.array(0, startPoint[1]))) #outlaboptimalDistY
							outlabXactual.append(outlabactx)
							outlabYactual.append(outlabacty)

						optimalDist = 0
						actualDist = 0
						startTime = 0
						prevTime = 0
						outlabactx = 0
						outlabacty = 0

					if(measuring == True):
						currentPos = np.array((float(row[3]), float(row[2])))
						localDistX = dist(np.array(prevPoint[0], 0), np.array(currentPos[0], 0))
						localDistY = dist(np.array(0, prevPoint[1]), np.array(0, currentpos[1]))
						outlabactX = float(outlabactX + localDistX)
						outlabactY = float(outlabactY + localDistY)
					
					prevPoint = np.array((float(row[3]), float(row[2])))
					prevTime = float(row[1])
			
			
			if(measuring == True):	
				if( ((float(row[1]) > lab1start) and (float(row[1]) < lab1end)) or ((float(row[1]) > lab2start) and (float(row[1]) < lab2end)) ):
					optimalDist = dist(prevPoint, startPoint)

					if(actualDist != 0 and (float(optimalDist/actualDist) != float(1.0)) and (startTime - prevTime >= float(0.0))):
						inlabXoptimal.append(dist(np.array(prevPoint[0], 0), np.array(startPoint[0], 0))) #inlaboptimalDistX
						inlabYoptimal.append(dist(np.array(0, prevPoint[1]), np.array(0, startPoint[1]))) #inlaboptimalDistY
						inlabXactual.append(inlabactx)
						inlabYactual.append(inlabacty)
				
					optimalDist = 0
					actualDist = 0
					startTime = 0
					prevTime = 0
					measuring = False
					inlabactx = 0
					inlabacty = 0


				else:					

					if(actualDist != 0 and (float(optimalDist/actualDist) != float(1.0)) and (startTime - prevTime >= float(0.0))):
						outlabXoptimal.append(dist(np.array(prevPoint[0], 0), np.array(startPoint[0], 0))) #outlaboptimalDistX
						outlabYoptimal.append(dist(np.array(0, prevPoint[1]), np.array(0, startPoint[1]))) #outlaboptimalDistY
						outlabXactual.append(outlabactx)
						outlabYactual.append(outlabacty)

					optimalDist = 0
					actualDist = 0
					startTime = 0
					measuring = False
					prevTime = 0
					outlabactx = 0
					outlabacty = 0


			optimalDist = 0
			actualDist = 0
			startTime = 0
			prevTime = 0
			measuring = False	
			inlabactx = 0
			inlabacty = 0
			outlabactx = 0
			outlabacty = 0
		
		print filenum



inlabXactual = np.array(inlabXactual)
inlabXoptimal = np.array(inlabXoptimal)
inlabYactual = np.array(inlabyactual)
inlabYoptimal = np.array(inlabyoptimal)
outlabXactual = np.array(outlabxactual)
outlabXoptimal = np.array(outlabxoptimal)
outlabYactual = no.array(outlabyactual)
outlabYoptimal = np.array(outlabyoptimal)

print len(inlabXactual)
print len(inlabXoptimal)
print len(inlabYactual)
print len(inlabYoptimal)
print len(outlabXactual)
print len(outlabXoptimal)
print len(outlabYactual)
print len(outlabYoptimal)

c1 = csv.writer(handle1, delimiter = ',')
c2 = csv.writer(handle2, delimiter = ',')
c3 = csv.writer(handle3, delimiter = ',')
c4 = csv.writer(handle4, delimiter = ',')
c5 = csv.writer(handle5, delimiter = ',')
c6 = csv.writer(handle6, delimiter = ',')
c7 = csv.writer(handle7, delimiter = ',')
c8 = csv.writer(handle8, delimiter = ',')


c1.writerow(inlabxactual)
c2.writerow(inlabXoptimal)
c3.writerow(inlabyactual)
c4.writerow(inlabyoptimal)
c5.writerow(outlabxactual)
c6.writerow(outlabxoptimal)
c7.writerow(outlabyactual)
c8.writerow(outlabyoptimal)

'''
print len(totalinlabeff)
print len(totaloutlabeff)
print np.mean(totalinlabeff, dtype=np.float64)
print np.mean(totaloutlabeff, dtype=np.float64)
'''
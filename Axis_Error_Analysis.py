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

inlabactX = 0
inlabactY = 0
outlabactX = 0
outlabactY = 0


def dist(a, b):
	return float(np.linalg.norm(a-b))

for current_directory, directories, files in os.walk(rootdir):
	
	for file in files:
		filenum += 1
		filepath = os.path.join(current_directory,file)

		optimalDist = 0
		actualDist = 0
		startTime = 0
		prevTime = 0
		measuring = False
		inlabactX = 0
		inlabactY = 0
		outlabactX = 0
		outlabactY = 0

		with open(filepath) as infile:
			parsed = csv.reader(infile)

			for row in parsed:

				filename = row[0].lower().replace(" ", "-")

				# IN LAB
				if( ((float(row[1]) > lab1start) and (float(row[1]) < lab1end)) or ((float(row[1]) > lab2start) and (float(row[1]) < lab2end))):
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
							prevoptx = np.array((float(prevPoint[0]), float(5)))
							startoptx = np.array((float(startPoint[0]), float(5))) #inlaboptimalDistX
							optx = float(dist(prevoptx, startoptx))
							#print optx
							inlabXoptimal.append(optx)
							prevopty = np.array((5, float(prevPoint[1])))
							startopty = np.array((5, float(startPoint[1]))) #inlaboptimalDistX
							opty = float(dist(prevopty, startopty))
							#	print opty
							inlabYoptimal.append(opty)
							inlabXactual.append(inlabactX)
							inlabYactual.append(inlabactY)

						optimalDist = 0
						actualDist = 0
						startTime = 0
						prevTime = 0
						inlabactX = 0
						inlabactY = 0

					if(measuring == True):
						currentPos = np.array((float(row[3]), float(row[2])))
						localDist = dist(prevPoint, currentPos)
						actualDist = float(actualDist + localDist)
						prevlocalX = np.array((float(prevPoint[0]), float(5)))
						currentlocalX = np.array((float(currentPos[0]), float(5)))
						localDistX = dist(prevlocalX, currentlocalX)
						prevlocalY = np.array((float(5), float(prevPoint[1])))
						currentlocalY = np.array((float(6), float(currentPos[1])))
						localDistY = dist(prevlocalY, currentlocalY)
						inlabactX = float(inlabactX + localDistX)
						#print inlabactX
						inlabactY = float(inlabactY + localDistY)
						#print inlabactY

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
							prevoptx = np.array((float(prevPoint[0]), float(0)))
							startoptx = np.array((float(startPoint[0]), float(0))) #inlaboptimalDistX
							optx = float(dist(prevoptx, startoptx))
							outlabXoptimal.append(optx)
							prevopty = np.array((0, float(prevPoint[1])))
							startopty = np.array((0, float(startPoint[1]))) #inlaboptimalDistX
							opty = dist(prevopty, startopty)
							outlabYoptimal.append(opty)
							outlabXactual.append(inlabactX)
							outlabYactual.append(inlabactY)

						optimalDist = 0
						actualDist = 0
						startTime = 0
						prevTime = 0
						outlabactX = 0
						outlabactY = 0

					if(measuring == True):
						currentPos = np.array((float(row[3]), float(row[2])))
						localDist = dist(prevPoint, currentPos)
						actualDist = float(actualDist + localDist)
						prevlocalX = np.array((float(prevPoint[0]), float(0)))
						currentlocalX = np.array((float(currentPos[0]), float(0)))
						localDistX = dist(prevlocalX, currentlocalX)
						prevlocalY = np.array((float(0), float(prevPoint[1])))
						currentlocalY = np.array((float(0), float(currentPos[1])))
						localDistY = dist(prevlocalY, currentlocalY)
						inlabactX = float(inlabactX + localDistX)
						inlabactY = float(inlabactY + localDistY)
					
					prevPoint = np.array((float(row[3]), float(row[2])))
					prevTime = float(row[1])
			
			
			if(measuring == True):	
				if( ((float(row[1]) > lab1start) and (float(row[1]) < lab1end)) or ((float(row[1]) > lab2start) and (float(row[1]) < lab2end))):
					optimalDist = dist(prevPoint, startPoint)

					if(actualDist != 0 and (float(optimalDist/actualDist) != float(1.0)) and (startTime - prevTime >= float(0.0))):
						prevoptx = np.array((float(prevPoint[0]), float(0)))
						startoptx = np.array((float(startPoint[0]), float(0))) #inlaboptimalDistX
						optx = float(dist(prevoptx, startoptx))
						inlabXoptimal.append(optx)
						prevopty = np.array((0, float(prevPoint[1])))
						startopty = np.array((0, float(startPoint[1]))) #inlaboptimalDistX
						opty = dist(prevopty, startopty)
						inlabYoptimal.append(opty)
						inlabXactual.append(inlabactX)
						inlabYactual.append(inlabactY)
				
					optimalDist = 0
					actualDist = 0
					startTime = 0
					prevTime = 0
					measuring = False
					inlabactX = 0
					inlabactY = 0


				else:					

					if(actualDist != 0 and (float(optimalDist/actualDist) != float(1.0)) and (startTime - prevTime >= float(0.0))):
						prevoptx = np.array((float(prevPoint[0]), float(0)))
						startoptx = np.array((float(startPoint[0]), float(0))) #inlaboptimalDistX
						optx = float(dist(prevoptx, startoptx))
						outlabXoptimal.append(optx)
						prevopty = np.array((0, float(prevPoint[1])))
						startopty = np.array((0, float(startPoint[1]))) #inlaboptimalDistX
						opty = dist(prevopty, startopty)
						outlabYoptimal.append(opty)
						outlabXactual.append(inlabactX)
						outlabYactual.append(inlabactY)

					optimalDist = 0
					actualDist = 0
					startTime = 0
					measuring = False
					prevTime = 0
					outlabactX = 0
					outlabactY = 0


			optimalDist = 0
			actualDist = 0
			startTime = 0
			prevTime = 0
			measuring = False	
			inlabactX = 0
			inlabactY = 0
			outlabactX = 0
			outlabactY = 0
		
		print filenum


print len(inlabXactual)
print len(inlabXoptimal)
print len(inlabYactual)
print len(inlabYoptimal)
print len(outlabXactual)
print len(outlabXoptimal)
print len(outlabYactual)
print len(outlabYoptimal)

inlabXactual = np.array(inlabXactual)
inlabXoptimal = np.array(inlabXoptimal)
inlabYactual = np.array(inlabYactual)
inlabYoptimal = np.array(inlabYoptimal)
outlabXactual = np.array(outlabXactual)
outlabXoptimal = np.array(outlabXoptimal)
outlabYactual = np.array(outlabYactual)
outlabYoptimal = np.array(outlabYoptimal)

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


c1.writerow(inlabXactual)
c2.writerow(inlabXoptimal)
c3.writerow(inlabYactual)
c4.writerow(inlabYoptimal)
c5.writerow(outlabXactual)
c6.writerow(outlabXoptimal)
c7.writerow(outlabYactual)
c8.writerow(outlabYoptimal)

'''
print len(totalinlabeff)
print len(totaloutlabeff)
print np.mean(totalinlabeff, dtype=np.float64)
print np.mean(totaloutlabeff, dtype=np.float64)
'''
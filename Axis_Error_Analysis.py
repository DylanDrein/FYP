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

handle1 = open("./Metricstest/inlabxactual - copy.csv", 'wb')
handle2 = open("./Metricstest/inlabxoptimal - copy.csv", 'wb')
handle3 = open("./Metricstest/inlabyactual - copy.csv", 'wb')
handle4 = open("./Metricstest/inlabyoptimal - copy.csv", 'wb')
handle5 = open("./Metricstest/outlabxactual - copy.csv", 'wb')
handle6 = open("./Metricstest/outlabxoptimal - copy.csv", 'wb')
handle7 = open("./Metricstest/outlabyactual - copy.csv", 'wb')
handle8 = open("./Metricstest/outlabyoptimal - copy.csv", 'wb')

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
						startPoint = np.array((row[3], row[2])).astype(np.float64)
						prevPoint = np.array((row[3], row[2])).astype(np.float64)
						startTime = float(row[1])
						prevTime = float(row[1])
						
					if((float(row[1]) < (startTime - 1450) or row[4] == "mouseUp") and measuring):
						measuring = False
						optimalDist = dist(prevPoint, startPoint)

						#histogram
						if(actualDist != 0 and optimalDist !=0 and (optimalDist !=  actualDist) and (startTime - prevTime > float(0.0))):
							prevoptx = np.array((prevPoint[0], 0)).astype(np.float64)
							startoptx = np.array((startPoint[0], 0)).astype(np.float64) #inlaboptimalDistX
							#print optx
							prevopty = np.array((0, prevPoint[1])).astype(np.float64)
							startopty = np.array((0, startPoint[1])).astype(np.float64) #inlaboptimalDistX
							
							optx = dist(prevoptx, startoptx)
							if(optx != float(0)):
								inlabXoptimal.append(optx)

							opty = dist(prevopty, startopty)
							if(opty != float(0)):
								inlabYoptimal.append(opty)

							if(inlabactX != float(0)):
								inlabXactual.append(inlabactX)

							if(inlabactY != float(0)):
								inlabYactual.append(inlabactY)

						optimalDist = 0
						actualDist = 0
						startTime = 0
						prevTime = 0
						inlabactX = 0
						inlabactY = 0

					if(measuring == True):
						currentPos = np.array((row[3], row[2])).astype(np.float64)
						localDist = dist(prevPoint, currentPos)
						actualDist = float(actualDist + localDist)
						prevlocalX = np.array((prevPoint[0], 0)).astype(np.float64)
						currentlocalX = np.array((currentPos[0], 0)).astype(np.float64)
						localDistX = dist(prevlocalX, currentlocalX)
						prevlocalY = np.array((0, prevPoint[1])).astype(np.float64)
						currentlocalY = np.array((0, currentPos[1])).astype(np.float64)
						localDistY = dist(prevlocalY, currentlocalY)
						inlabactX = float(inlabactX + localDistX)
						#print inlabactX
						inlabactY = float(inlabactY + localDistY)
						#print inlabactY

					prevPoint = np.array((row[3], row[2])).astype(np.float64)
					prevTime = float(row[1])
					
				# OUT OF LAB
				else:
					if(row[4] == "mouseDown"):
						measuring = True
						startPoint = np.array((row[3], row[2])).astype(np.float64)
						prevPoint = np.array((row[3], row[2])).astype(np.float64)
						startTime = float(row[1])
						prevTime = float(row[1])
						
					if((float(row[1]) < (startTime - 1450) or row[4] == "mouseUp") and measuring):
						measuring = False
						optimalDist = dist(prevPoint, startPoint)

						#histogram
						if(actualDist != 0 and optimalDist !=0 and (optimalDist !=  actualDist) and (startTime - prevTime > float(0.0))):
							prevoptx = np.array((prevPoint[0], 0)).astype(np.float64)
							startoptx = np.array((startPoint[0], 0)).astype(np.float64) #inlaboptimalDistX
							prevopty = np.array((0, prevPoint[1])).astype(np.float64)
							startopty = np.array((0, startPoint[1])).astype(np.float64) #inlaboptimalDistX
							
							optx = dist(prevoptx, startoptx)
							if(optx != float(0)):
								outlabXoptimal.append(optx)

							opty = dist(prevopty, startopty)
							if(opty != float(0)):
								outlabYoptimal.append(opty)

							if(inlabactX != float(0)):
								outlabXactual.append(outlabactX)

							if(inlabactY != float(0)):
								outlabYactual.append(outlabactY)

						optimalDist = 0
						actualDist = 0
						startTime = 0
						prevTime = 0
						outlabactX = 0
						outlabactY = 0

					if(measuring == True):
						currentPos = np.array((row[3], row[2])).astype(np.float64)
						localDist = dist(prevPoint, currentPos)
						actualDist = float(actualDist + localDist)
						prevlocalX = np.array((prevPoint[0], 0)).astype(np.float64)
						currentlocalX = np.array((currentPos[0], 0)).astype(np.float64)
						localDistX = dist(prevlocalX, currentlocalX)
						prevlocalY = np.array((0, prevPoint[1])).astype(np.float64)
						currentlocalY = np.array((0, currentPos[1])).astype(np.float64)
						localDistY = dist(prevlocalY, currentlocalY)
						outlabactX = float(outlabactX + localDistX)
						outlabactY = float(outlabactY + localDistY)
					
					prevPoint = np.array((row[3], row[2])).astype(np.float64)
					prevTime = float(row[1])
			
			
			if(measuring == True):	
				if( ((float(row[1]) > lab1start) and (float(row[1]) < lab1end)) or ((float(row[1]) > lab2start) and (float(row[1]) < lab2end))):
					optimalDist = dist(prevPoint, startPoint)

					if(actualDist != 0 and optimalDist !=0 and (optimalDist !=  actualDist) and (startTime - prevTime > float(0.0))):
						prevoptx = np.array((prevPoint[0], 0)).astype(np.float64)
						startoptx = np.array((startPoint[0], 0)).astype(np.float64) #inlaboptimalDistX
						prevopty = np.array((0, prevPoint[1])).astype(np.float64)
						startopty = np.array((0, startPoint[1])).astype(np.float64) #inlaboptimalDistX

						optx = dist(prevoptx, startoptx)
						if(optx != float(0)):
							inlabXoptimal.append(optx)

						opty = dist(prevopty, startopty)
						if(opty != float(0)):
							inlabYoptimal.append(opty)

						if(inlabactX != float(0)):
							inlabXactual.append(inlabactX)

						if(inlabactY != float(0)):
							inlabYactual.append(inlabactY)
				
					optimalDist = 0
					actualDist = 0
					startTime = 0
					prevTime = 0
					measuring = False
					inlabactX = 0
					inlabactY = 0

				else:					
					if(actualDist != 0 and optimalDist !=0 and (optimalDist !=  actualDist) and (startTime - prevTime > float(0.0))):
						prevoptx = np.array((prevPoint[0], 0)).astype(np.float64)
						startoptx = np.array((startPoint[0], 0)).astype(np.float64) #inlaboptimalDistX
						
						prevopty = np.array((0, prevPoint[1])).astype(np.float64)
						startopty = np.array((0, startPoint[1])).astype(np.float64) #inlaboptimalDistX
						
						optx = dist(prevoptx, startoptx)
						if(optx != float(0)):
							outlabXoptimal.append(optx)

						opty = dist(prevopty, startopty)
						if(opty != float(0)):
							outlabYoptimal.append(opty)

						if(inlabactX != float(0)):
							outlabXactual.append(outlabactX)

						if(inlabactY != float(0)):
							outlabYactual.append(outlabactY)

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

inlabXactual = np.array(inlabXactual).astype(np.float64)
inlabXoptimal = np.array(inlabXoptimal).astype(np.float64)
inlabYactual = np.array(inlabYactual).astype(np.float64)
inlabYoptimal = np.array(inlabYoptimal).astype(np.float64)
outlabXactual = np.array(outlabXactual).astype(np.float64)
outlabXoptimal = np.array(outlabXoptimal).astype(np.float64)
outlabYactual = np.array(outlabYactual).astype(np.float64)
outlabYoptimal = np.array(outlabYoptimal).astype(np.float64)

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
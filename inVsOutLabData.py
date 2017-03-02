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

'''
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
'''


totalinlabeff = []
totaloutlabeff = []
totalinlabtimes = []
totaloutlabtimes = []


lab1start = 1415358000000 # 11am 7th november
lab1end = 1415365200000 # 1pm

lab2start = 1417172400000 # 11am 28th of november
lab2end = 1417179600000 # 1pm

handle1 = open("./Efficiencies/inlab.csv", 'wb')
handle2 = open("./Efficiencies/outlab.csv", 'wb')
handle3 = open("./Efficiencies/inlabtimes.csv", 'wb')
handle4 = open("./Efficiencies/outlabtimes.csv", 'wb')

filename = ""

def dist(a, b):
	return float(np.linalg.norm(a-b))

for current_directory, directories, files in os.walk(rootdir):
	
	for file in files:
		filenum += 1
		filepath = os.path.join(current_directory,file)
		measuring = False

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
						
					if((float(row[1]) < (startTime - 1500) or row[4] == "mouseUp") and measuring):
						measuring = False
						optimalDist = dist(prevPoint, startPoint)

						#histogram
						if(actualDist != 0):
							totalinlabeff.append(float(optimalDist/actualDist))
							totalinlabtimes.append(startTime - prevTime)


						optimalDist = 0
						actualDist = 0
						startTime = 0

					if(measuring == True):
						currentPos = np.array((float(row[3]), float(row[2])))
						localDist = dist(prevPoint, currentPos)
						actualDist = float(actualDist + localDist)

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
						

					if((float(row[1]) < (startTime - 1500) or row[4] == "mouseUp") and measuring):
						measuring = False
						optimalDist = float(dist(prevPoint, startPoint))

						#histogram
						if(actualDist != 0):
							totaloutlabeff.append(float(optimalDist/actualDist))
							totaloutlabtimes.append(startTime - prevTime)


						optimalDist = 0
						actualDist = 0
						startTime = 0

					if(measuring == True):
						currentPos = np.array((float(row[3]), float(row[2])))
						localDist = float(dist(prevPoint, currentPos))
						actualDist = float(actualDist + localDist)


					prevPoint = np.array((float(row[3]), float(row[2])))
					prevTime = float(row[1])
			
			
			if(measuring == True):	
				if( ((float(row[1]) > lab1start) and (float(row[1]) < lab1end)) or ((float(row[1]) > lab2start) and (float(row[1]) < lab2end)) ):
					optimalDist = dist(prevPoint, startPoint)

					if(actualDist != 0):
						totalinlabeff.append(float(optimalDist/actualDist))
						totalinlabtimes.append(startTime - prevTime)


					optimalDist = 0
					actualDist = 0
					startTime = 0

				else:
					optimalDist = dist(prevPoint, startPoint)
					
					if(actualDist != 0):
						totaloutlabeff.append(float(optimalDist/actualDist))
						totaloutlabtimes.append(startTime - prevTime)


					optimalDist = 0
					actualDist = 0
					startTime = 0
					measuring = False


		print filenum



totalinlabeff = np.array(totalinlabeff)
totaloutlabeff = np.array(totaloutlabeff)
totalinlabtimes = np.array(totalinlabtimes)
totaloutlabtimes = np.array(totaloutlabtimes)

'''
print len(totalinlabeff)
print len(totalinlabtimes)
print len(totaloutlabeff)
print len(totaloutlabtimes)
'''



c1 = csv.writer(handle1, delimiter = ',')
c2 = csv.writer(handle2, delimiter = ',')
c3 = csv.writer(handle3, delimiter = ',')
c4 = csv.writer(handle4, delimiter = ',')


c1.writerow(totalinlabeff)
c2.writerow(totaloutlabeff)
c3.writerow(totalinlabtimes)
c4.writerow(totaloutlabtimes)


'''
print len(totalinlabeff)
print len(totaloutlabeff)
print np.mean(totalinlabeff, dtype=np.float64)
print np.mean(totaloutlabeff, dtype=np.float64)
print totaloutlabeff
'''
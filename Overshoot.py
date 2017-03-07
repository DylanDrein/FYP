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
startPoint = []
startTime = 0
prevPoint = []
measuring = False

filenum = 0

inlabovershoot = []
outlabovershoot = []

lab1start = 1415358000000 # 11am 7th november
lab1end = 1415365200000 # 1pm

lab2start = 1417172400000 # 11am 28th of november
lab2end = 1417179600000 # 1pm

handle1 = open("./Metrics/inlabovershoot.csv", 'wb')
handle2 = open("./Metrics/outlabovershoot.csv", 'wb')

filename = ""

def dist(a, b):
	return float(np.linalg.norm(a-b))

for current_directory, directories, files in os.walk(rootdir):
	
	for file in files:
		filenum += 1
		filepath = os.path.join(current_directory,file)

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
						
					if((float(row[1]) < (startTime - 1450) or row[4] == "mouseUp") and measuring):
						measuring = False
						actualDist = 0
						startTime = 0
						

					if(measuring == True):
						currentPos = np.array((float(row[3]), float(row[2])))
						localDist = dist(prevPoint, currentPos)
						actualDist = float(actualDist + localDist)

						if(row[4] != "mouseDown" and (np.array_equal(currentPos, startPoint))):
							inlabovershoot.append(actualDist)

					prevPoint = np.array((float(row[3]), float(row[2])))
					

				# OUT OF LAB
				else:
					if(row[4] == "mouseDown"):
						measuring = True
						startPoint = np.array((float(row[3]), float(row[2])))
						prevPoint = np.array((float(row[3]), float(row[2])))
						startTime = float(row[1])
						
					if((float(row[1]) < (startTime - 1450) or row[4] == "mouseUp") and measuring):
						measuring = False
						actualDist = 0
						startTime = 0

					if(measuring == True):
						currentPos = np.array((float(row[3]), float(row[2])))
						localDist = float(dist(prevPoint, currentPos))
						actualDist = float(actualDist + localDist)

						if(row[4] != "mouseDown" and (np.array_equal(currentPos, startPoint))):
							outlabovershoot.append(actualDist)
						
					prevPoint = np.array((float(row[3]), float(row[2])))
			
			if(measuring == True):	
				if( ((float(row[1]) > lab1start) and (float(row[1]) < lab1end)) or ((float(row[1]) > lab2start) and (float(row[1]) < lab2end)) ):
					if(row[4] != "mouseDown" and (np.array_equal(currentPos, startPoint))):
						inlabovershoot.append(actualDist)

					actualDist = 0
					startTime = 0
					measuring = False

				else:
					if(row[4] != "mouseDown" and (np.array_equal(currentPos, startPoint))):
						outlabovershoot.append(actualDist)

					actualDist = 0
					startTime = 0
					measuring = False

			else:
				actualDist = 0
				startTime = 0
				measuring = False
	
		print filenum


print len(inlabovershoot)
print len(outlabovershoot)

c1 = csv.writer(handle7, delimiter = ',')
c2 = csv.writer(handle8, delimiter = ',')

c1.writerow(inlabovershoot)
c2.writerow(outlabovershoot)
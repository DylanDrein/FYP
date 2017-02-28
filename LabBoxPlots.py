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

inlabeff = []
outlabeff = []

totalinlabeff = []
totaloutlabeff = []

hourmilliseconds = 3600000

lab1start = 1415358000000 # 11am 7th november
lab1end = 1415365200000 # 1pm

lab2start = 1417172400000 # 11am 28th of november
lab2end = 1417179600000 # 1pm

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
							inlabeff.append(float(optimalDist/actualDist))
							totalinlabeff.append(float(optimalDist/actualDist))
						
							#actualVals1.append(actualDist)
							#optimalVals1.append(optimalDist)
							#times1.append(startTime)

						optimalDist = 0
						actualDist = 0
						startTime = 0

					if(measuring == True):
						currentPos = np.array((float(row[3]), float(row[2])))
						currentTime = float(row[1])
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
							outlabeff.append(float(optimalDist/actualDist))
							totaloutlabeff.append(float(optimalDist/actualDist))
						
							#actualVals2.append(actualDist)
							#optimalVals2.append(optimalDist)
							#times2.append(startTime)

						optimalDist = 0
						actualDist = 0
						startTime = 0

					if(measuring == True):
						currentPos = np.array((float(row[3]), float(row[2])))
						currentTime = float(row[1])
						localDist = float(dist(prevPoint, currentPos))
						actualDist = float(actualDist + localDist)


					prevPoint = np.array((float(row[3]), float(row[2])))
					prevTime = float(row[1])
			
			
			if(measuring == True):	
				if( ((float(row[1]) > lab1start) and (float(row[1]) < lab1end)) or ((float(row[1]) > lab2start) and (float(row[1]) < lab2end)) ):
					optimalDist = dist(prevPoint, startPoint)

					if(actualDist != 0):
						inlabeff.append(float(optimalDist/actualDist))
						totalinlabeff.append(float(optimalDist/actualDist))

						#actualVals1.append(actualDist)
						#optimalVals1.append(optimalDist)
						#times1.append(startTime)

					optimalDist = 0
					actualDist = 0
					startTime = 0

				else:
					optimalDist = dist(prevPoint, startPoint)
					
					if(actualDist != 0):
						outlabeff.append(float(optimalDist/actualDist))
						totaloutlabeff.append(float(optimalDist/actualDist))

						#actualVals2.append(actualDist)
						#optimalVals2.append(optimalDist)
						#times2.append(startTime)

					optimalDist = 0
					actualDist = 0
					startTime = 0
					measuring = False

		
		#totalinlabeff.append(inlabeff)
		#totaloutlabeff.append(float(optimalDist/actualDist))

		'''
		inlabeff = np.array(inlabeff)
		outlabeff = np.array(outlabeff)

		data = [inlabeff, outlabeff]
		plt.boxplot(data, 0, '')
		plt.title("Box plots of in lab efficiency (left) vs. out of lab efficiency (right)")
		plt.ylabel('Efficiency (optimal/actual path lengths')
		plt.savefig('./LabBoxPlots/' + filename + '.png')
		plt.clf()
		'''

		inlabeff = []
		outlabeff = []
		del inlabeff[:]
		del outlabeff[:]

		print filenum

#totalinlabeff = np.asarray((totalinlabeff)).astype(float)
#totaloutlabeff = np.asarray((totaloutlabeff)).astype(float)

#print totaloutlabeff

totaloutlabeff = np.array(totaloutlabeff)
totalinlabeff = np.array(totalinlabeff)

print len(totalinlabeff)
print len(totaloutlabeff)
print np.mean(totalinlabeff, dtype=np.float64)
print np.mean(totaloutlabeff, dtype=np.float64)
#print totaloutlabeff
'''
data = [totalinlabeff, totaloutlabeff]
plt.boxplot(data, 0, '')
plt.title("Total in lab efficiency (left) vs. Total out of lab efficiency (right)")
plt.ylabel('Efficiency (optimal/actual path lengths')
plt.savefig('./LabBoxPlots/' + "xtotal" + '.png')
plt.clf()
'''
import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

#handle1 = open("./Metrics/outlabtimes.csv", 'rb')

handle1 = open("./Metrics/outlab.csv", 'rb')
handle2 = open("./Metrics/inlab.csv", 'rb')

handle3 = open("./Metrics/outlabtimes1.csv", 'rb')
handle4 = open("./Metrics/inlabtimes.csv", 'rb')

handle5 = open("./Metrics/outlabspeed.csv", 'rb')
handle6 = open("./Metrics/inlabspeed.csv", 'rb')


inlab = []
outlab = []
inlabtimes = []
outlabtimes = []
inlabspeed = []
outlabspeed = []

'''
with handle1 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		print len(row)
		for place in range(0, len(row)):
			#print row[place]
			if(float(row[place]) <= float(0.0)):
				print row[place]
				
			else:
				outlabtimes.append(row[place])
				
'''

with handle1 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		print len(row)

with handle2 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		print len(row)

with handle3 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		print len(row)

with handle4 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		print len(row)

with handle5 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		print len(row)

with handle6 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		print len(row)


#print len(outlabtimes)

#c1 = csv.writer(handle2, delimiter = ',')

#c1.writerow(outlabtimes)
import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

# Earliest UNIX time = 1412364244763 , Fri, 03 Oct 2014 19:24:04.763 GMT

'''
Get earliest date from results of SemesterTimeWrite script
Find the date and then get midnight from that day
create hist by adding multiples of 86400 onto that unix time
'''

#handle = open("./MouseDownEvents/MouseClicktimes.csv", 'rb')

filepath = "./MouseDownEvents/MouseClicktimes.csv"

times = []


firstMidnight = 1412290800000
daySeconds = 86400

with open(filepath) as infile:
			
	parsed=csv.reader(infile)
	for row in parsed:
		times = np.array(list(row)).astype(np.float)


bins = np.arange(firstMidnight, np.amax(times), 86400)

#print max(bins) - min(bins) % daySeconds

plt.hist(times, bins, facecolor='green')
plt.title("$Histogram$ $of$ $Optimal/Actual$ $path$ $lengths$")
plt.xlabel("$Value$")
plt.ylabel("$Frequency$")
plt.savefig('./Histograms/' + "SemesterTimeWrite" + '.png')
plt.clf()

import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

# Earliest UNIX time = 1412364244763 , Fri, 03 Oct 2014 19:24:04.763 GMT

'''
Histograms of specific lab exam days, broken down by hour.
'''

#handle = open("./MouseDownEvents/MouseClicktimes.csv", 'rb')

handle1 = open("./LabDayMouseEvents/lab1.csv", 'r')
handle2 = open("./LabDayMouseEvents/lab2.csv", 'r')

times1 = []
times2 = []

daymilliseconds = 86400000
hourmilliseconds = 3600000

#firstlabmidnight = 1415232000000 # 6th of november
firstlabmidnight = 1415318400000 # 7th of november
secondlabmidnight = 1417132800000 # 28th of november

with handle1 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		times1 = np.array(list(row)).astype(np.float)

with handle2 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		times2 = np.array(list(row)).astype(np.float)

bins1 = range(firstlabmidnight, firstlabmidnight + daymilliseconds, hourmilliseconds)
bins2 = range(secondlabmidnight, secondlabmidnight + daymilliseconds, hourmilliseconds)

#print type(bins1)
#print type(bins2)
#print int(times1[0])

hours = range(0, 2500, 100)

#print np.arange(firstlabmidnight, firstlabmidnight + daymilliseconds, hourmilliseconds)


plt.hist(times1, bins = bins1, facecolor='green', label="1 bin = 1 hour")
plt.title("mouseDown events over first lab exam day")
plt.xlabel("Hours (24-hr format)")
plt.ylabel("# of mouseDown events")
#plt.xticks(np.arange(firstlabmidnight, firstlabmidnight + daymilliseconds, hourmilliseconds), rotation = 'vertical')
plt.xticks(bins1, hours, rotation = 'vertical')
plt.subplots_adjust(bottom=0.15)
plt.legend()
plt.savefig('./Histograms/' + "Lab1" + '.png')
plt.clf()

plt.hist(times2, bins = bins2, facecolor='green', label="1 bin = 1 hour")
plt.title("mouseDown events over first lab exam day")
plt.xlabel("Hours (24-hr format)")
plt.ylabel("# of mouseDown events")
#plt.xticks(np.arange(secondlabmidnight, secondlabmidnight + daymilliseconds, hourmilliseconds), rotation = 'vertical')
plt.xticks(bins2, hours, rotation = 'vertical')
plt.subplots_adjust(bottom=0.15)
plt.legend()
plt.savefig('./Histograms/' + "Lab2" + '.png')
plt.clf()

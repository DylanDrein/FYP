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

handle1 = open("./LabWeekMouseEvents/LabWeek1.csv", 'rb')
handle2 = open("./LabWeekMouseEvents/LabWeek2.csv", 'rb')

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


bins1 = range(firstlabmidnight - 3*(daymilliseconds), firstlabmidnight + 3*(daymilliseconds), hourmilliseconds)
bins2 = range(secondlabmidnight - 3*(daymilliseconds), secondlabmidnight + 3*(daymilliseconds), hourmilliseconds)

x1 = range(len(times1))
x2 = range(len(times2))

#print type(bins1)
#print type(bins2)
#print int(times1[0])

hours = np.arange(0, 2500, 100)

#print np.arange(firstlabmidnight, firstlabmidnight + daymilliseconds, hourmilliseconds)


plt.hist(times1, bins = bins1, facecolor='green', label="1 bin = 1 hour")
plt.title("mouseDown events over first lab exam week")
plt.xlabel("Hours (24-hr format)")
plt.ylabel("# of mouseDown events")
#plt.xticks(np.arange(firstlabmidnight, firstlabmidnight + daymilliseconds, hourmilliseconds), rotation = 'vertical')
#plt.xticks(bins1, ["{:d}".format(int(v)) for v in hours], rotation = 'vertical')
#plt.xticklabels(["{:d}".format(int(v)) for v in hours]) 
#plt.subplots_adjust(bottom=0.15)
xposition = range(firstlabmidnight - 3*(daymilliseconds), firstlabmidnight + 3*(daymilliseconds), daymilliseconds)
for xc in xposition:
    plt.axvline(x=xc, color='r', linestyle='solid', linewidth = 0.5)
plt.legend()
plt.savefig('./Histograms/' + "LabWeek1" + '.png')
plt.clf()

plt.hist(times2, bins = bins2, facecolor='green', label="1 bin = 1 hour")
plt.title("mouseDown events over second lab exam week")
plt.xlabel("Hours")
plt.ylabel("# of mouseDown events")
#plt.xticks(np.arange(secondlabmidnight, secondlabmidnight + daymilliseconds, hourmilliseconds), rotation = 'vertical')
#plt.xticks(bins2, ["{:d}".format(int(v)) for v in hours], rotation = 'vertical')
##plt.xticklabels(["{:d}".format(int(v)) for v in hours]) 
#plt.xticks(bins2, hours, rotation = 'vertical')
#plt.subplots_adjust(bottom=0.15)
xposition = range(secondlabmidnight - 3*(daymilliseconds), secondlabmidnight + 3*(daymilliseconds), daymilliseconds)
for xc in xposition:
    plt.axvline(x=xc, color='r', linestyle='solid', linewidth = 0.5)
plt.legend()
plt.savefig('./Histograms/' + "LabWeek2" + '.png')
plt.clf()

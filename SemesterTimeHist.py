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

filepath = "./AllMouseDownEvents/MouseClicktimes.csv"

times = []


firstMidnight = 1412290800000
daymilliseconds = 86400000

firstlabmidnight = 1415232000000 # 6th of november
#firstlabmidnight = 1415318400000 # 7th of november
secondlabmidnight = 1417132800000 # 28th of november

with open(filepath) as infile:
			
	parsed=csv.reader(infile)
	for row in parsed:
		times = np.array(list(row)).astype(np.float)


#print int(min(times))
#print int(max(times))


bins = range(firstMidnight, max(times), daymilliseconds)

#print max(bins) - min(bins) % daySeconds
plt.clf()
plt.hist(times, bins, facecolor='green', label="$1$ $bin$ $=$ $1$ $day$")
plt.title("$mouseDown$ $Events$ $Over$ $Semester$")
plt.xlabel("$UNIX$ $epoch$ $time$")
plt.ylabel("$Number$ $of$ $mouseDown$ $Events$")
xposition = [firstlabmidnight, firstlabmidnight + daymilliseconds, secondlabmidnight, secondlabmidnight + daymilliseconds]
for xc in xposition:
    plt.axvline(x=xc, color='r', linestyle='solid', linewidth = 0.5)
plt.legend()
plt.savefig('./Histograms/' + "SemesterTimeWrite" + '.png')
plt.clf()

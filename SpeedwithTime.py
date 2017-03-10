import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

handle3 = open("./Metricstest/inlabspeed.csv", 'rb')
handle4 = open("./Metricstest/outlabspeed.csv", 'rb')
handle5 = open("./Metricstest/inlabtimes.csv", 'rb')
handle6 = open("./Metricstest/outlabtimes.csv", 'rb')


inlabspeed = []
outlabspeed = []
inlabtimes = []
outlabtimes = []


with handle3 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inlabspeed = np.array(list(row)).astype(np.float)

with handle4 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabspeed = np.array(list(row)).astype(np.float)

with handle5 as infile:
	parsed = csv.reader(infile)
	for row in parsed:
		inlabtimes = np.array(list(row)).astype(np.float)

with handle6 as infile:
	parsed = csv.reader(infile)
	for row in parsed:
		outlabtimes = np.array(list(row)).astype(np.float)

bins = np.arange(0, 2000, 20)

#print len(inlabspeed)
#print len(outlabspeed)
#print len(inlabtimes)
#print len(outlabtimes)

#inlabspeed = np.log(inlabspeed)
#outlabspeed = np.log(outlabspeed)

inlabspeed = 1000*(np.array(inlabspeed))
outlabspeed = 1000*(np.array(outlabspeed))

#inlabspeed = (np.array(inlabspeed))
#outlabspeed = (np.array(outlabspeed))

sdvinlab = np.std(inlabspeed)
meaninlab = np.mean(inlabspeed)
varinlab = np.var(inlabspeed)
sdvoutlab = np.std(outlabspeed)
meanoutlab = np.mean(outlabspeed)
varoutlab = np.var(outlabspeed)


label1 = ["$\overline{x}$ = " + str(meaninlab) + "\n" + "$s$ = " + str(sdvinlab) + "\n" + "$s^2$ = " + str(varinlab)]
plt.hist(inlabspeed, bins, label = label1)
#plt.hist(inlabspeed, bins, label = label1)
plt.title("Histogram of mouse movement speed in lab environment")
plt.xlabel("Speed $(px/s)$")
plt.ylabel("Frequency (# of mouse movements)")
#plt.xticks(np.arange(0, 1.1, 0.1), rotation = 'vertical')
plt.legend(loc="best")
#plt.show()
plt.savefig('./finalgraphs/In_Lab_Speed_Histogram_Unweighted.png')
plt.clf()

label2 = ["$\overline{x}$ = " + str(meanoutlab) + "\n" + "$s$ = " + str(sdvoutlab) + "\n" + "$s^2$ = " + str(varoutlab)]
plt.hist(outlabspeed, bins, label = label2)
#plt.hist(outlabspeed, bins, label = label2)
plt.title("Histogram of mouse movement speed out of lab environment")
plt.xlabel("Speed $(px/s)$")
plt.ylabel("Frequency (# of mouse movements)")
#plt.xticks(np.arange(0, 1.1, 0.1), rotation = 'vertical')
plt.legend(loc="best")
#plt.show()
plt.savefig('./finalgraphs/Out_Of_Lab_Speed_Histogram_Unweighted.png')
plt.clf()


print meaninlab
print sdvinlab
print varinlab
print meanoutlab
print sdvoutlab
print varoutlab

print max(inlabspeed)
print max(outlabspeed)


data = [inlabspeed, outlabspeed]
plt.boxplot(data, 0, '', labels=["In lab", "Out of lab"])
plt.title("Speed of mouse sequence")
plt.ylabel("Speed $(px/s)$")
#plt.savefig('./finalgraphs/' + "TotalBoxPlot" + '.png')
plt.show()
plt.clf()

import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt


handle5 = open("./Metricstest/inlabspeed.csv", 'rb')
handle6 = open("./Metricstest/outlabspeed.csv", 'rb')
handle7 = open("./Metricstest/inlabovershoot.csv", 'rb')
handle8 = open("./Metricstest/outlabovershoot.csv", 'rb')


inlabspeed = []
outlabspeed = []
inlabovershoot = []
outlabovershoot = []


with handle5 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inlabspeed = np.array(list(row)).astype(np.float)

with handle6 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabspeed = np.array(list(row)).astype(np.float)

with handle7 as infile:
	parsed = csv.reader(infile)
	for row in parsed:
		inlabovershoot = np.array(list(row)).astype(np.float)

with handle8 as infile:
	parsed = csv.reader(infile)
	for row in parsed:
		outlabovershoot = np.array(list(row)).astype(np.float)

bins = np.arange(0, 225, 5)

#print len(inlabspeed)
#print len(outlabspeed)
#print len(inlabovershoot)
#print len(outlabovershoot)

#inlabspeed = np.log(inlabovershoot)
#outlabspeed = np.log(inlabovershoot)

sdvinlab = np.std(inlabovershoot)
meaninlab = np.mean(inlabovershoot)
varinlab = np.var(inlabovershoot)
sdvoutlab = np.std(outlabovershoot)
meanoutlab = np.mean(outlabovershoot)
varoutlab = np.var(inlabovershoot)

label1 = ["$\overline{x}$ = " + str(meaninlab) + "\n" + "$s$ = " + str(sdvinlab) + "\n" + "$s^2$ = " + str(varinlab)]
plt.hist(inlabovershoot, bins, label = label1)
plt.title("Histogram of mouse path overshoot in lab environment")
plt.xlabel("Overshoot (px)")
plt.ylabel("Frequency (# of mouse path sequences)")
plt.xticks(np.arange(0, 225, 25), rotation = 'vertical')
plt.legend(loc="best")
#plt.show()
plt.savefig('./finalgraphs/In_Lab_Overshoot_Histogram_Unweighted.png')
plt.clf()

label2 = ["$\overline{x}$ = " + str(meanoutlab) + "\n" + "$s$ = " + str(sdvoutlab) + "\n" + "$s^2$ = " + str(varoutlab)]
plt.hist(outlabovershoot, bins, label = label2)
plt.title("Histogram of mouse path overshoot out of lab environment")
plt.xlabel("Overshoot (px)")
plt.ylabel("Frequency (# of mouse path sequences)")
plt.xticks(np.arange(0, 225, 25), rotation = 'vertical')
plt.legend(loc="best")
#plt.show()
plt.savefig('./finalgraphs/Out_Of_Lab_Overshoot_Histogram_Unweighted.png')
plt.clf()

print meaninlab
print sdvinlab
print varinlab
print meanoutlab
print sdvoutlab
print varoutlab
print max(inlabovershoot)
print max(outlabovershoot)


data = [inlabspeed, outlabspeed]
plt.boxplot(data, 0, '', labels=["In lab", "Out of lab"])
plt.title("Total in lab mouse path overshoot")
plt.ylabel('speediciency (optimal/actual path lengths')
plt.savefig('./finalgraphs/Total_Overshoot_BoxPlot_No_Outliers_No_Notches.png')
#plt.show()
plt.clf()
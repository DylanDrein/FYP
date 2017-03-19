import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

handle1 = open("./Metricstest/inlabeff.csv", 'rb')
handle2 = open("./Metricstest/outlabeff.csv", 'rb')
handle3 = open("./Metricstest/inlabtimes.csv", 'rb')
handle4 = open("./Metricstest/outlabtimes.csv", 'rb')

inlabeff = []
outlabeff = []
inlabtimes = []
outlabtimes = []


with handle1 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inlabeff = np.array(list(row)).astype(np.float)

with handle2 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabeff = np.array(list(row)).astype(np.float)

with handle3 as infile:
	parsed = csv.reader(infile)
	for row in parsed:
		inlabtimes = np.array(list(row)).astype(np.float)

with handle4 as infile:
	parsed = csv.reader(infile)
	for row in parsed:
		outlabtimes = np.array(list(row)).astype(np.float)


bins = np.arange(0, 1.01, 0.01)

#print len(inlabeff)
#print len(outlabeff)
#print len(inlabtimes)
#print len(outlabtimes)

#inlabeff = np.log2(inlabeff)
#outlabeff = np.log2(outlabeff)

#print inlabeff
#print outlabeff
'''
inlabeff = np.ma.masked_equal(inlabeff,0)
outlabeff = np.ma.masked_equal(outlabeff,0)

sdvinlab = np.std(inlabeff)
meaninlab = np.mean(inlabeff)
varinlab = np.var(inlabeff)
sdvoutlab = np.std(outlabeff)
meanoutlab = np.mean(outlabeff)
varoutlab = np.var(outlabeff)
'''

inlabtimes = np.ma.masked_equal(inlabtimes,0)
outlabtimes = np.ma.masked_equal(outlabtimes,0)

sdvinlab = np.std(inlabtimes)
meaninlab = np.mean(inlabtimes)
varinlab = np.var(inlabtimes)
sdvoutlab = np.std(outlabtimes)
meanoutlab = np.mean(outlabtimes)
varoutlab = np.var(outlabtimes)
'''
label1 = ["$\overline{x}$ = " + str(meaninlab) + "\n" + "$s$ = " + str(sdvinlab) + "\n" + "$s^2$ = " + str(varinlab)]
plt.hist(inlabeff, bins, label = label1)
#plt.hist(inlabeff, bins, label = label1)
#plt.title("Probability density $f(x)$ of in-lab mousepath efficiency \n weighted by duration of mouse sequence")
plt.title("Histogram of mousepath efficiency in lab environment")
plt.xlabel("Efficiency (Optimal mousepath length / Actual mousepath length)")
plt.ylabel("Frequency (# mouse path sequences)")
#plt.ylabel("Weighted probability density $f(x)$")
#plt.xticks(np.arange(0, 1.1, 0.1), rotation = 'vertical')
plt.legend(loc="best")
#plt.show()
plt.savefig('./FinalGraphs/InLabEfficiencyHist.png')
#plt.savefig('./Metricgraphs/' + "WeightedinLabHist" + '.png')
plt.clf()

label2 = ["$\overline{x}$ = " + str(meanoutlab) + "\n" + "$s$ = " + str(sdvoutlab) + "\n" + "$s^2$ = " + str(varoutlab)]
plt.hist(outlabeff, bins, label = label2)
#plt.hist(outlabeff, bins, label = label2)
#plt.title("Probability density $f(x)$ of out-of-lab mousepath efficiency \n weighted by duration of mouse sequence")
plt.title("Histogram of mousepath efficiency out of lab environment")
plt.xlabel("Efficiency (Optimal mousepath length / Actual mousepath length)")
plt.ylabel("Frequency (# mouse path sequences)")
#plt.xticks(np.arange(0, 1.1, 0.1), rotation = 'vertical')
plt.legend(loc="best")
#plt.show()
plt.savefig('./FinalGraphs/OutLabEfficiencyHist.png')
#plt.savefig('./Metricgraphs/' + "WeightedOutOfLabHist" + '.png')
plt.clf()
'''
print meaninlab
print sdvinlab
print varinlab
print meanoutlab
print sdvoutlab
print varoutlab
print min(inlabtimes)
print max(inlabtimes)
print min(outlabtimes)
print max(outlabtimes)

'''
data = [inlabeff, outlabeff]
plt.boxplot(data, 0, '', labels=["In lab", "Out of lab"])
plt.title("Efficiency boxplot")
plt.ylabel('Efficiency (optimal/actual path lengths)')
#plt.savefig('./FinalGraphs/TotalEfficiencyBoxPlotNoNotchesNoOutliers.png')
plt.show()
plt.clf()
'''
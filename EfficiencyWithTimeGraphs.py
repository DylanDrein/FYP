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

print len(inlabeff)
print len(outlabeff)
print len(inlabtimes)
print len(outlabtimes)

#inlabeff = np.log(inlabeff)
#outlabeff = np.log(outlabeff)

sdvinlab = np.std(inlabeff)
meaninlab = np.mean(inlabeff)
label1 = ["$\mu$: " + str(meaninlab) + "\n" + "$\sigma$: " + str(sdvinlab)]
plt.hist(inlabeff, bins, label = label1)
#plt.hist(inlabeff, bins, label = label1)
#plt.title("Probability density $f(x)$ of in-lab mousepath efficiency \n weighted by duration of mouse sequence")
plt.title("Histogram of in-lab mousepath efficiency")
plt.xlabel("Efficiency (Optimal mousepath length / Actual mousepath length)")
plt.ylabel("# of mouse path sequences")
#plt.ylabel("Weighted probability density $f(x)$")
#plt.xticks(np.arange(0, 1.1, 0.1), rotation = 'vertical')
plt.legend(loc="best")
plt.show()
plt.savefig('./FinalGraphs/InLabEfficiencyHist.png')
#plt.savefig('./Metricgraphs/' + "PDFinLab" + '.png')
#plt.savefig('./Metricgraphs/' + "WeightedinLabHist" + '.png')
#plt.savefig('./Metricgraphs/' + "WeightedinLabPDF" + '.png')
plt.clf()

sdvoutlab = np.std(outlabeff)
meanoutlab = np.mean(outlabeff)
label2 = ["$\mu$: " + str(meanoutlab) + "\n" + "$\sigma$: " + str(sdvoutlab)]
plt.hist(outlabeff, bins, label = label2)
#plt.hist(outlabeff, bins, label = label2)
#plt.title("Probability density $f(x)$ of out-of-lab mousepath efficiency \n weighted by duration of mouse sequence")
plt.title("Histogram of out-of-lab mousepath efficiency")
plt.xlabel("Efficiency (Optimal mousepath length / Actual mousepath length)")
plt.ylabel("# of mouse path sequences")
#plt.ylabel("Weighted probability density $f(x)$")
#plt.xticks(np.arange(0, 1.1, 0.1), rotation = 'vertical')
plt.legend(loc="best")
plt.show()
plt.savefig('./FinalGraphs/OutLabEfficiencyHist.png')
#plt.savefig('./Metricgraphs/' + "PDFOutOfLab" + '.png')
#plt.savefig('./Metricgraphs/' + "WeightedOutOfLabHist" + '.png')
#plt.savefig('./Metricgraphs/' + "WeightedOutOfLabPDF" + '.png')
plt.clf()


print sdvinlab
print meaninlab
print sdvoutlab
print meanoutlab


'''
data = [inlabeff, outlabeff]
plt.boxplot(data, 1)
plt.title("Total in lab efficiency (left) vs. Total out of lab efficiency (right)")
plt.ylabel('Efficiency (optimal/actual path lengths')
#plt.savefig('./Metricgraphs/' + "TotalBoxPlot" + '.png')
plt.show()
plt.clf()
'''
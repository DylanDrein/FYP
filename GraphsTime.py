import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

handleintimes = open("./Metricstest/inlabtimes.csv", 'rb')
handleouttimes = open("./Metricstest/outlabtimes.csv", 'rb')

inlabtimes = []
outlabtimes = []


with handleintimes as infile:
	parsed = csv.reader(infile)
	for row in parsed:
		inlabtimes = np.array(list(row)).astype(np.float)

with handleouttimes as infile:
	parsed = csv.reader(infile)
	for row in parsed:
		outlabtimes = np.array(list(row)).astype(np.float)

bins = np.arange(0, 1480, 10)

'''
#print len(inlabtimes)
#print len(outlabtimes)
#print len(inlabtimes)
#print len(outlabtimes)


print np.var(inlabeff)
print np.var(outlabeff)
print np.var(inlabtimes)
print np.var(outlabtimes)
print np.var(inlabspeeds)
print np.var(outlabspeeds)


#print inlabtimes
#print outlabtimes

'''


#speed, change back when done!!!
inlabtimes = np.array(inlabtimes)
outlabtimes = np.array(outlabtimes)

sdvinlab = np.std(inlabtimes)
meaninlab = np.mean(inlabtimes)
label1 = ["$\mu$: " + str(meaninlab) + "\n" + "$\sigma$: " + str(sdvinlab)]
plt.hist(inlabtimes, bins, label = label1)
#plt.hist(inlabtimes, bins, label = label1)
#plt.title("Probability density $f(x)$ of in-lab mousepath efficiency \n weighted by duration of mouse sequence")
plt.title("Histogram of mouse path time length in lab")
plt.xlabel("Mouse path sequence time duration")
#plt.ylabel("# of mouse path sequences")
plt.ylabel("Number of mouse path sequences")
plt.xticks(np.arange(0, 1480, 100), rotation = 'vertical')
plt.legend(loc="best")
plt.show()
#plt.savefig('./Metricgraphs/' + "inLabPDFexcl" + '.png')
#plt.savefig('./Metricgraphs/' + "PDFinLab" + '.png')
#plt.savefig('./Metricgraphs/' + "WeightedinLabHist" + '.png')
#plt.savefig('./Metricgraphs/' + "inLabTimeHist1" + '.png')
plt.clf()

sdvoutlab = np.std(outlabtimes)
meanoutlab = np.mean(outlabtimes)
label2 = ["$\mu$: " + str(meanoutlab) + "\n" + "$\sigma$: " + str(sdvoutlab)]
plt.hist(outlabtimes, bins, label = label2)
#plt.hist(outlabtimes, bins, label = label2)
#plt.title("Probability density $f(x)$ of out-of-lab mousepath efficiency \n weighted by duration of mouse sequence")
plt.title("Histogram of mouse path time length out of lab")
plt.xlabel("Mouse path sequence time duration")
#plt.ylabel("# of mouse path sequences")
plt.ylabel("Number of mouse path sequences")
plt.xticks(np.arange(0, 1480, 100), rotation = 'vertical')
plt.legend(loc="best")
plt.show()
#plt.savefig('./Metricgraphs/' + "OutOfLabPDFexcl" + '.png')
#plt.savefig('./Metricgraphs/' + "PDFOutOfLab" + '.png')
#plt.savefig('./Metricgraphs/' + "WeightedOutOfLabHist" + '.png')
#plt.savefig('./Metricgraphs/' + "outLabTimeHist1" + '.png')
plt.clf()


#print sdvinlab
#print meaninlab
#print sdvoutlab
#print meanoutlab

'''
data = [inlabtimes, outlabtimes]
plt.boxplot(data, 1)
plt.title("Total in lab efficiency (left) vs. Total out of lab efficiency (right)")
plt.ylabel('Efficiency (optimal/actual path lengths')
#plt.savefig('./Metricgraphs/' + "TotalBoxPlot" + '.png')
plt.show()
plt.clf()

'''
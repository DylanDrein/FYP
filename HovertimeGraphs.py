import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt


handle9 = open("./Metricstest/inlabhovertime.csv", 'rb')
handle10 = open("./Metricstest/outlabhovertime.csv", 'rb')

inlabhover = []
outlabhover = []


with handle9 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inlabhover = np.array(list(row)).astype(np.float)

with handle10 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabhover = np.array(list(row)).astype(np.float)

bins = np.arange(0, 1500, 10)

#print len(inlabhover)
#print len(outlabhover)
#print len(inlabtimes)
#print len(outlabtimes)

#inlabhover = np.log(inlabhover)
#outlabhover = np.log(outlabhover)


sdvinlab = np.std(inlabhover)
meaninlab = np.mean(inlabhover)
varinlab = np.var(inlabhover)
sdvoutlab = np.std(outlabhover)
meanoutlab = np.mean(outlabhover)
varoutlab = np.var(outlabhover)

label1 = ["$\overline{x}$ = " + str(meaninlab) + "\n" + "$s$ = " + str(sdvinlab) + "\n" + "$s^2$ = " + str(varinlab)]
plt.hist(inlabhover, bins, label = label1)
#plt.hist(inlabhover, bins, label = label1)
plt.title("Histogram of hover time duration before mouse click \n in lab environment")
#plt.title("Histogram of in-lab mousepath efficiency")
plt.xlabel("Hover time duration (ms)")
plt.ylabel("Frequency (# of mouse path sequences)")
#plt.xticks(np.arange(0, 1.1, 0.1), rotation = 'vertical')
plt.legend(loc="best")
plt.show()
#plt.savefig('./Metricgraphs/' + "inLabPDFexcl" + '.png')
#plt.savefig('./Metricgraphs/' + "PDFinLab" + '.png')
#plt.savefig('./Metricgraphs/' + "WeightedinLabHist" + '.png')
#plt.savefig('./Metricgraphs/' + "WeightedinLabPDF" + '.png')
plt.clf()


label2 = ["$\overline{x}$ = " + str(meanoutlab) + "\n" + "$s$ = " + str(sdvoutlab) + "\n" + "$s^2$ = " + str(varoutlab)]
plt.hist(outlabhover, bins, label = label2)
#plt.hist(outlabhover, bins, label = label2)
plt.title("Histogram of hover time duration before mouse click \n out of lab environment")
#plt.title("Histogram of out-of-lab mousepath efficiency")
plt.xlabel("Hover time duration (ms)")
plt.ylabel("Frequency (# of mouse path sequences)")
#plt.xticks(np.arange(0, 1.1, 0.1), rotation = 'vertical')
plt.legend(loc="best")
plt.show()
#plt.savefig('./Metricgraphs/' + "OutOfLabPDFexcl" + '.png')
#plt.savefig('./Metricgraphs/' + "PDFOutOfLab" + '.png')
#plt.savefig('./Metricgraphs/' + "WeightedOutOfLabHist" + '.png')
#plt.savefig('./Metricgraphs/' + "WeightedOutOfLabPDF" + '.png')
plt.clf()


print meaninlab
print sdvinlab
print varinlab
print meanoutlab
print sdvoutlab
print varoutlab


data = [inlabhover, outlabhover]
plt.boxplot(data, 0, '', labels=["In lab", "Out of lab"])
plt.title("Mouse hover time before click event")
plt.ylabel('Hover time (ms)')
#plt.savefig('./Metricgraphs/' + "TotalBoxPlot" + '.png')
plt.show()
plt.clf()

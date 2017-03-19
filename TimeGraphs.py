import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt


handle1 = open("./Metricstest/inlabtimes.csv", 'rb')
handle2 = open("./Metricstest/outlabtimes.csv", 'rb')


inlabtimes = []
outlabtimes = []


with handle1 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inlabtimes = np.array(list(row)).astype(np.float64)

with handle2 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabtimes = np.array(list(row)).astype(np.float64)


bins = np.arange(0, 1470, 20)

#print len(inlabtimes)
#print len(outlabtimes)
#print len(inlabtimes)
#print len(outlabtimes)

#inlabtimes = np.log(inlabtimes)
#outlabtimes = np.log(outlabtimes)


sdvinlab = np.std(inlabtimes)
meaninlab = np.mean(inlabtimes)
varinlab = np.var(inlabtimes)
label1 = ["$\overline{x}$ = " + str(meaninlab) + "\n" + "$s$ = " + str(sdvinlab) + "\n" + "$s^2$ = " + str(varinlab)]
plt.hist(inlabtimes, bins, label = label1)
#plt.hist(inlabtimes, bins, label = label1)
plt.title("Histogram of mouse path sequence \n time durations in lab environment")
#plt.title("Histogram of in-lab mousepath efficiency")
plt.xlabel("Time (ms)")
plt.ylabel("Frequency (# of mouse path sequences)")
plt.xticks(np.arange(0, 1550, 100), rotation = 'vertical')
plt.legend(loc="best")
plt.show()
plt.savefig('./finalgraphs/In_Lab_Time_Histogram.png')
#plt.savefig('./finalgraphs/' + "PDFinLab" + '.png')
#plt.savefig('./finalgraphs/' + "WeightedinLabHist" + '.png')
#plt.savefig('./finalgraphs/' + "WeightedinLabPDF" + '.png')
plt.clf()

sdvoutlab = np.std(outlabtimes)
meanoutlab = np.mean(outlabtimes)
varoutlab = np.var(outlabtimes)
label2 = ["$\overline{x}$ = " + str(meanoutlab) + "\n" + "$s$ = " + str(sdvoutlab) + "\n" + "$s^2$ = " + str(varoutlab)]
plt.hist(outlabtimes, bins, label = label2)
#plt.hist(outlabtimes, bins, label = label2)
plt.title("Histogram of mouse path sequence time durations out of lab environment")
#plt.title("Histogram of out-of-lab mousepath efficiency")
plt.xlabel("Time (ms)")
plt.ylabel("Frequency (# of mouse path sequences)")
plt.xticks(np.arange(0, 1550, 100), rotation = 'vertical')
plt.legend(loc="best")
plt.show()
plt.savefig('./finalgraphs/Out_Of_Lab_Time_Histogram.png')
#plt.savefig('./finalgraphs/' + "PDFOutOfLab" + '.png')
#plt.savefig('./finalgraphs/' + "WeightedOutOfLabHist" + '.png')
#plt.savefig('./finalgraphs/' + "WeightedOutOfLabPDF" + '.png')
plt.clf()



print sdvinlab
print meaninlab
print sdvoutlab
print meanoutlab


'''
data = [inlabtimes, outlabtimes]
plt.boxplot(data, 0, '', labels=["In lab", "Out of lab"])
plt.title("Mouse path sequence time length")
plt.ylabel('Time (ms)')
#plt.savefig('./finalgraphs/' + "TotalBoxPlot" + '.png')
plt.show()
plt.clf()
'''
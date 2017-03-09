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
		inlabtimes = np.array(list(row)).astype(np.float)

with handle2 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabtimes = np.array(list(row)).astype(np.float)


#bins = np.arange(0, 7, 0.1)

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
plt.title("Probability density $f(x)$ of in-lab mousepath efficiency \n weighted by duration of mouse sequence")
#plt.title("Histogram of in-lab mousepath efficiency")
plt.xlabel("Efficiency (Optimal mousepath length / Actual mousepath length)")
#plt.ylabel("# of mouse path sequences")
plt.ylabel("Weighted probability density $f(x)$")
#plt.xticks(np.arange(0, 1.1, 0.1), rotation = 'vertical')
plt.legend(loc="best")
plt.show()
#plt.savefig('./finalgraphs/' + "inLabPDFexcl" + '.png')
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
plt.title("Probability density $f(x)$ of out-of-lab mousepath efficiency \n weighted by duration of mouse sequence")
#plt.title("Histogram of out-of-lab mousepath efficiency")
plt.xlabel("Efficiency (Optimal mousepath length / Actual mousepath length)")
#plt.ylabel("# of mouse path sequences")
plt.ylabel("Weighted probability density $f(x)$")
#plt.xticks(np.arange(0, 1.1, 0.1), rotation = 'vertical')
plt.legend(loc="best")
plt.show()
#plt.savefig('./finalgraphs/' + "OutOfLabPDFexcl" + '.png')
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
plt.boxplot(data, 1)
plt.title("Total in lab efficiency (left) vs. Total out of lab efficiency (right)")
plt.ylabel('Efficiency (optimal/actual path lengths')
#plt.savefig('./finalgraphs/' + "TotalBoxPlot" + '.png')
plt.show()
plt.clf()
'''
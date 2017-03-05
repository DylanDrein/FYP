import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

handleintimes = open("./Efficienciestest/inlabspeed.csv", 'rb')
handleouttimes = open("./Efficienciestest/outlabspeed.csv", 'rb')

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

#bins = np.arange(0, 2000, 50)

#print len(inlabtimes)
#print len(outlabtimes)
#print len(inlabtimes)
#print len(outlabtimes)

#speed, change back when done!!!
inlabtimes = np.log(inlabtimes)
outlabtimes = np.log(outlabtimes)

print inlabtimes
print outlabtimes

print np.var(inlabeff)
print np.var(outlabeff)
print np.var(inlabtimes)
print np.var(outlabtimes)
print np.var(inlabspeeds)
print np.var(outlabspeeds)

'''
sdvinlab = np.std(inlabtimes)
meaninlab = np.mean(inlabtimes)
label1 = ["$\mu$: " + str(meaninlab) + "\n" + "$\sigma$: " + str(sdvinlab)]
plt.hist(inlabtimes, label = label1)
#plt.hist(inlabtimes, bins, label = label1)
#plt.title("Probability density $f(x)$ of in-lab mousepath efficiency \n weighted by duration of mouse sequence")
plt.title("Histogram of mouse path time length in lab")
plt.xlabel("Mouse path sequence time duration")
#plt.ylabel("# of mouse path sequences")
plt.ylabel("Number of mouse path sequences")
#plt.xticks(np.arange(0, 1.1, 0.1), rotation = 'vertical')
plt.legend(loc="best")
plt.show()
#plt.savefig('./EfficiencyGraphs/' + "inLabPDFexcl" + '.png')
#plt.savefig('./EfficiencyGraphs/' + "PDFinLab" + '.png')
#plt.savefig('./EfficiencyGraphs/' + "WeightedinLabHist" + '.png')
#plt.savefig('./EfficiencyGraphs/' + "inLabTimeHist1" + '.png')
plt.clf()

sdvoutlab = np.std(outlabtimes)
meanoutlab = np.mean(outlabtimes)
label2 = ["$\mu$: " + str(meanoutlab) + "\n" + "$\sigma$: " + str(sdvoutlab)]
plt.hist(outlabtimes, label = label2)
#plt.hist(outlabtimes, bins, label = label2)
#plt.title("Probability density $f(x)$ of out-of-lab mousepath efficiency \n weighted by duration of mouse sequence")
plt.title("Histogram of mouse path time length out of lab")
plt.xlabel("Mouse path sequence time duration")
#plt.ylabel("# of mouse path sequences")
plt.ylabel("Number of mouse path sequences")
#plt.xticks(np.arange(0, 1.1, 0.1), rotation = 'vertical')
plt.legend(loc="best")
plt.show()
#plt.savefig('./EfficiencyGraphs/' + "OutOfLabPDFexcl" + '.png')
#plt.savefig('./EfficiencyGraphs/' + "PDFOutOfLab" + '.png')
#plt.savefig('./EfficiencyGraphs/' + "WeightedOutOfLabHist" + '.png')
#plt.savefig('./EfficiencyGraphs/' + "outLabTimeHist1" + '.png')
plt.clf()


#print sdvinlab
#print meaninlab
#print sdvoutlab
#print meanoutlab



data = [inlabtimes, outlabtimes]
plt.boxplot(data, 1)
plt.title("Total in lab efficiency (left) vs. Total out of lab efficiency (right)")
plt.ylabel('Efficiency (optimal/actual path lengths')
#plt.savefig('./EfficiencyGraphs/' + "TotalBoxPlot" + '.png')
plt.show()
plt.clf()
'''

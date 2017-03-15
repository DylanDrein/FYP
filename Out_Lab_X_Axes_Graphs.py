import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

handle1 = open("./metricstest/outlabxactual - copy.csv", 'rb')
handle2 = open("./metricstest/outlabxoptimal - copy.csv", 'rb')

#np.seterr(divide="raise")

outlabxact = []
outlabxopt = []

with handle1 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabxact = np.array(list(row)).astype(np.float64)

with handle2 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabxopt = np.array(list(row)).astype(np.float64)

absolutesubtract = np.subtract(outlabxopt, outlabxact)
absoluteerror = np.abs(absolutesubtract)
#outlabxoptabs = np.abs(outlabxopt)

#absoluteerror = np.true_divide(absoluteerror, outlabxoptabs)

#print absoluteerror

#print absoluteerror

outlabxoptabs = np.abs(outlabxopt)

relativeerror = np.true_divide(absoluteerror, outlabxoptabs)

sdvoutxrel = np.std(relativeerror)
meanoutxrel = np.mean(relativeerror)
varoutxrel = np.var(relativeerror)

print relativeerror
print sdvoutxrel
print meanoutxrel
print varoutxrel


'''
sdvoutlab = np.std(absoluteerror)
meanoutlab = np.mean(absoluteerror)
varoutlab = np.var(absoluteerror)

bins = np.arange(0, 250, 2)
label1 = ["$\overline{x}$ = " + str(meanoutlab) + "\n" + "$s$ = " + str(sdvoutlab) + "\n" + "$s^2$ = " + str(varoutlab) + "\n" + "Max value: " + str(max(absoluteerror)) + "\n" + "Min value: " + str(min(absoluteerror))]
plt.hist(absoluteerror, bins, label = label1)
plt.title("Absolute error in Click Sequence limited to x-axis movement out of lab environment")
plt.xlabel("Error (px)")
plt.ylabel("Frequency (# of mouse path sequences)")
plt.legend(loc="best")
plt.xticks(np.arange(0, max(bins), 10), rotation = 'vertical')
plt.savefig('./FinalGraphs/Out_Lab_X-Axis_Absolute_Error.png')
plt.clf()
'''
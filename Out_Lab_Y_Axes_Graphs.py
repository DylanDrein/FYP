import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

handle1 = open("./metricstest/outlabyactual - copy.csv", 'rb')
handle2 = open("./metricstest/outlabyoptimal - copy.csv", 'rb')

#np.seterr(divide="raise")

outlabyact = []
outlabyopt = []

with handle1 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabyact = np.array(list(row)).astype(np.float64)

with handle2 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabyopt = np.array(list(row)).astype(np.float64)

absolutesubtract = np.subtract(outlabyopt, outlabyact)
absoluteerror = np.abs(absolutesubtract)
#outlabyoptabs = np.abs(outlabyopt)

#absoluteerror = np.true_divide(absoluteerror, outlabyoptabs)

#print absoluteerror

#print absoluteerror

outlabyoptabs = np.abs(outlabyopt)

relativeerror = np.true_divide(absoluteerror, outlabyoptabs)

print relativeerror

'''
sdvoutlab = np.std(absoluteerror)
meanoutlab = np.mean(absoluteerror)
varoutlab = np.var(absoluteerror)

bins = np.arange(0, 250, 2)
label1 = ["$\overline{x}$ = " + str(meanoutlab) + "\n" + "$s$ = " + str(sdvoutlab) + "\n" + "$s^2$ = " + str(varoutlab) + "\n" + "Max value: " + str(max(absoluteerror)) + "\n" + "Min value: " + str(min(absoluteerror))]
plt.hist(absoluteerror, bins, label = label1)
plt.title("Absolute error in Click Sequence limited to y-axis movement out of lab environment")
plt.xlabel("Error (px)")
plt.ylabel("Frequency (# of mouse path sequences)")
plt.legend(loc="best")
plt.xticks(np.arange(0, max(bins), 10), rotation = 'vertical')
plt.savefig('./FinalGraphs/Out_Lab_Y-Axis_Absolute_Error.png')
plt.clf()
'''
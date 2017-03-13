import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

handle1 = open("./metricstest/inlabyactual - copy.csv", 'rb')
handle2 = open("./metricstest/inlabyoptimal - copy.csv", 'rb')

#np.seterr(divide="raise")

inlabyact = []
inlabyopt = []

with handle1 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inlabyact = np.array(list(row)).astype(np.float64)

with handle2 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inlabyopt = np.array(list(row)).astype(np.float64)

absolutesubtract = np.subtract(inlabyopt, inlabyact)
absoluteerror = np.abs(absolutesubtract)
#inlabyoptabs = np.abs(inlabyopt)

#absoluteerror = np.true_divide(absoluteerror, inlabyoptabs)

print absoluteerror

#print absoluteerror

sdvinlab = np.std(absoluteerror)
meaninlab = np.mean(absoluteerror)
varinlab = np.var(absoluteerror)

bins = np.arange(0, 250, 2)
label1 = ["$\overline{x}$ = " + str(meaninlab) + "\n" + "$s$ = " + str(sdvinlab) + "\n" + "$s^2$ = " + str(varinlab) + "\n" + "Max value: " + str(max(absoluteerror)) + "\n" + "Min value: " + str(min(absoluteerror))]
plt.hist(absoluteerror, bins, label = label1)
plt.title("Absolute error in y-axis movement in lab environment")
plt.xlabel("Error (px)")
plt.ylabel("Frequency (# of mouse path sequences)")
plt.legend(loc="best")
plt.savefig('./FinalGraphs/In_Lab_Y-Axis_Absolute_Error.png')
plt.clf()
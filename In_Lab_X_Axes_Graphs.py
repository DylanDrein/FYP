import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

handle1 = open("./metricstest/inlabxactual - copy.csv", 'rb')
handle2 = open("./metricstest/inlabxoptimal - copy.csv", 'rb')

#np.seterr(divide="raise")

inlabxact = []
inlabxopt = []

with handle1 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inlabxact = np.array(list(row)).astype(np.float64)

with handle2 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inlabxopt = np.array(list(row)).astype(np.float64)

absolutesubtract = np.subtract(inlabxopt, inlabxact)
absoluteerror = np.abs(absolutesubtract)
#inlabxoptabs = np.abs(inlabxopt)

#absoluteerror = np.true_divide(absoluteerror, inlabxoptabs)

print absoluteerror

#print absoluteerror

sdvinlab = np.std(absoluteerror)
meaninlab = np.mean(absoluteerror)
varinlab = np.var(absoluteerror)

bins = np.arange(0, 250, 1)
label1 = ["$\overline{x}$ = " + str(meaninlab) + "\n" + "$s$ = " + str(sdvinlab) + "\n" + "$s^2$ = " + str(varinlab) + "\n" + "Max value: " + str(max(absoluteerror)) + "\n" + "Min value: " + str(min(absoluteerror))]
plt.hist(absoluteerror, bins, label = label1)
plt.title("Absolute error in x-axis movement in lab environment")
plt.xlabel("Error (px)")
plt.ylabel("Frequency (# of mouse path sequences)")
plt.legend(loc="best")
plt.show()

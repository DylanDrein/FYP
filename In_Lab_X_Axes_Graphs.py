import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import stats

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

#print absoluteerror

#print absoluteerror

	

sdvinlab = np.std(absoluteerror)
meaninlab = np.mean(absoluteerror)
varinlab = np.var(absoluteerror)



#eff = np.true_divide(inlabxopt, inlabxact)

bins = np.arange(0, 250, 2)
label1 = ["$\overline{x}$ = " + str(meaninlab) + "\n" + "$s$ = " + str(sdvinlab) + "\n" + "$s^2$ = " + str(varinlab) + "\n" + "Max value: " + str(max(absoluteerror)) + "\n" + "Min value: " + str(min(absoluteerror))]
plt.hist(absoluteerror, bins, label = label1)
plt.title("Absolute error in Click Sequence x-axis movement in lab environment")
plt.xlabel("Error (px)")
plt.ylabel("Frequency (# of mouse path sequences)")
plt.legend(loc="best")
#plt.xticks(np.arange(0, max(bins), 10), rotation = 'vertical')
plt.savefig('./FinalGraphs/In_Lab_X-Axis_Absolute_Error.png')
#plt.show()
plt.clf()

#print min(eff)
#print max(eff)


#print scipy.stats.ttest_rel(inlabxopt, inlabxact)

#inlabxeff = np.true_divide(inlabxopt, inlabxact)
#print max(inlabxeff)
'''
absoluteerrorlog = np.log(inlabxopt)
sdvinlablog = np.std(absoluteerrorlog)
meaninlablog = np.mean(absoluteerrorlog)
varinlablog = np.var(absoluteerrorlog)

#bins = np.arange(0, 250, 2)
label1 = ["$\overline{x}$ = " + str(meaninlablog) + "\n" + "$s$ = " + str(sdvinlablog) + "\n" + "$s^2$ = " + str(varinlablog) + "\n" + "Max value: " + str(max(inlabxopt)) + "\n" + "Min value: " + str(min(inlabxopt))]
plt.hist(absoluteerrorlog, label = label1)
plt.title("Log of absolute error in x-axis movement in lab environment")
plt.xlabel("Log of error (px)")
plt.ylabel("Frequency (# of mouse path sequences)")
plt.legend(loc="best")
#plt.xticks(np.arange(0, max(bins), 10), rotation = 'vertical')
#plt.savefig('./FinalGraphs/In_Lab_X-Axis_Absolute_Error.png')
plt.show()
plt.clf()

inlabxeff = np.true_divide(inlabxopt, inlabxact)
print max(inlabxeff)


sdvinlabeff = np.std(inlabxeff)
meaninlabeff = np.mean(inlabxeff)
varinlabeff = np.var(inlabxeff)

label1 = ["$\overline{x}$ = " + str(meaninlabeff) + "\n" + "$s$ = " + str(sdvinlabeff) + "\n" + "$s^2$ = " + str(varinlabeff) + "\n" + "Max value: " + str(max(inlabxeff)) + "\n" + "Min value: " + str(min(inlabxeff))]
plt.hist(inlabxeff, label = label1)
plt.title("Efficiency in x-axis movement in lab environment")
plt.xlabel("Efficiency (Optimal distance in x-axis/Actual distance in x-axis)")
plt.ylabel("Frequency (# of Click Sequences)")
plt.legend(loc="best")
#plt.xticks(np.arange(0, max(bins), 10), rotation = 'vertical')
#plt.savefig('./FinalGraphs/In_Lab_X-Axis_Absolute_Error.png')
plt.show()
plt.clf()
'''
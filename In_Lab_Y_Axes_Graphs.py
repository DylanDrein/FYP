import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

handle1 = open("./metricstest/inlabyactual - copy.csv", 'rb')
handle2 = open("./metricstest/inlabyoptimal - copy.csv", 'rb')

handle3 = open("./metricstest/outlabyactual - copy.csv", 'rb')
handle4 = open("./metricstest/outlabyoptimal - copy.csv", 'rb')

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

outlabyact = []
outlabyopt = []

with handle3 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabyact = np.array(list(row)).astype(np.float64)
 
with handle4 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabyopt = np.array(list(row)).astype(np.float64)

outabsolutesubtract = np.subtract(outlabyopt, outlabyact)
outabsoluteerror = np.abs(outabsolutesubtract)

inabsolutesubtract = np.subtract(inlabyopt, inlabyact)
inabsoluteerror = np.abs(inabsolutesubtract)

inlabyoptabs = np.abs(inlabyopt)
outlabyoptabs = np.abs(outlabyopt)

inrelativeerror = np.true_divide(inabsoluteerror, inlabyoptabs)
outrelativeerror = np.true_divide(outabsoluteerror, outlabyoptabs)

inrelativeerror = np.ma.masked_equal(inrelativeerror,0.0)
outrelativeerror = np.ma.masked_equal(outrelativeerror,0.0)

meaninlab = np.mean(inrelativeerror)
sdvinlab = np.std(inrelativeerror)
varinlab = np.var(inrelativeerror)
meanoutlab = np.mean(outrelativeerror)
sdvoutlab = np.std(outrelativeerror)
varoutlab = np.var(outrelativeerror)

print meaninlab
print sdvinlab
print varinlab
print meanoutlab
print sdvoutlab
print varoutlab
print min(inrelativeerror)
print max(inrelativeerror)
print min(outrelativeerror)
print max(outrelativeerror)

#absoluteerror = np.true_divide(absoluteerror, inlabyoptabs)

#print absoluteerror

#print absoluteerror

'''
sdvinlab = np.std(absoluteerror)
meaninlab = np.mean(absoluteerror)
varinlab = np.var(absoluteerror)

bins = np.arange(0, 250, 2)
label1 = ["$\overline{x}$ = " + str(meaninlab) + "\n" + "$s$ = " + str(sdvinlab) + "\n" + "$s^2$ = " + str(varinlab) + "\n" + "Max value: " + str(max(absoluteerror)) + "\n" + "Min value: " + str(min(absoluteerror))]
plt.hist(absoluteerror, bins, label = label1)
plt.title("Absolute error in Click Sequence limited to y-axis movement in lab environment")
plt.xlabel("Error (px)")
plt.ylabel("Frequency (# of mouse path sequences)")
plt.legend(loc="best")
plt.savefig('./FinalGraphs/In_Lab_Y-Axis_Absolute_Error.png')
plt.clf()
'''
'''
inlabyoptabs = np.abs(inlabyopt)

relativeerror = np.square(np.true_divide(absoluteerror, inlabyoptabs))
sdvinxrel = np.std(relativeerror)
meaninxrel = np.mean(relativeerror)
varinxrel = np.var(relativeerror)

#bins = np.arange(0, 7000, 100)
label1 = ["$\overline{x}$ = " + str(meaninxrel) + "\n" + "$s$ = " + str(sdvinxrel) + "\n" + "$s^2$ = " + str(varinxrel) + "\n" + "Max value: " + str(max(relativeerror)) + "\n" + "Min value: " + str(min(relativeerror))]
plt.hist(relativeerror, bins, label = label1)
plt.title("Relative error in Click Sequence limited to \n y-axis movement in lab environment")
plt.xlabel("Relative error (px)")
plt.ylabel("Frequency (# of mouse path sequences)")
plt.legend(loc="best")
#plt.xticks(np.arange(0, max(bins), 10), rotation = 'vertical')
#plt.savefig('./FinalGraphs/In_Lab_X-Axis_Relative_Error.png')
plt.show()
plt.clf()

print relativeerror
print sdvinxrel
print meaninxrel
print varinxrel
'''

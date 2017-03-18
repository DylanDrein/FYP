import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import stats


handleineff = open("./Metricstest/inlabeff.csv", 'rb')
handleouteff = open("./Metricstest/outlabeff.csv", 'rb')

handleintimes = open("./Metricstest/inlabtimes.csv", 'rb')
handleouttimes = open("./Metricstest/outlabtimes.csv", 'rb')

handleinspeed = open("./Metricstest/inlabspeed.csv", 'rb')
handleoutspeed = open("./Metricstest/outlabspeed.csv", 'rb')

#overshoot
handleinovershoot = open("./Metricstest/inlabovershoot.csv", 'rb')
handleoutovershoot = open("./Metricstest/outlabovershoot.csv", 'rb')

#hovertime
handleinhovertime = open("./Metricstest/inlabhovertime.csv", 'rb')
handleouthovertime = open("./Metricstest/outlabhovertime.csv", 'rb')

#x axis
handleinxact = open("./metricstest/inlabxactual - copy.csv", 'rb')
handleinxopt = open("./metricstest/inlabxoptimal - copy.csv", 'rb')
handleoutxact = open("./metricstest/outlabxactual - copy.csv", 'rb')
handleoutxopt = open("./metricstest/outlabxoptimal - copy.csv", 'rb')

#y axis
handleinyact = open("./metricstest/inlabyactual - copy.csv", 'rb')
handleinyopt = open("./metricstest/inlabyoptimal - copy.csv", 'rb')
handleoutyact = open("./metricstest/outlabyactual - copy.csv", 'rb')
handleoutyopt = open("./metricstest/outlabyoptimal - copy.csv", 'rb')


inlabeff = []
outlabeff = []

inlabtimes = []
outlabtimes = []

inlabspeeds = []
outlabspeeds = []

inovershoot = []
outovershoot = []

inhovertime = []
outhovertime = []

inlabxact = []
inlabxopt = []

outlabxact = []
outlabxopt = []

inlabyact = []
inlabyopt = []

outlabyact = []
outlabyopt = []


with handleineff as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inlabeff = np.array(list(row)).astype(np.float32) 


with handleouteff as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabeff = np.array(list(row)).astype(np.float32)


with handleintimes as infile:
	parsed = csv.reader(infile)
	for row in parsed:
		inlabtimes = np.array(list(row)).astype(np.float32)

with handleouttimes as infile:
	parsed = csv.reader(infile)
	for row in parsed:
		outlabtimes = np.array(list(row)).astype(np.float32)


with handleinspeed as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inlabspeeds = np.array(list(row)).astype(np.float32)

with handleoutspeed as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabspeeds = np.array(list(row)).astype(np.float32)



with handleinovershoot as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inovershoot = np.array(list(row)).astype(np.float32)

with handleoutovershoot as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outovershoot = np.array(list(row)).astype(np.float32)

with handleinhovertime as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inhovertime = np.array(list(row)).astype(np.float32)

with handleouthovertime as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outhovertime = np.array(list(row)).astype(np.float32)

#inhovertime = np.ma.masked_equal(inhovertime,0.0)
#outhovertime = np.ma.masked_equal(outhovertime,0.0)

with handleinxact as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inlabxact = np.array(list(row)).astype(np.float64)

with handleinxopt as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inlabxopt = np.array(list(row)).astype(np.float64)

with handleoutxact as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabxact = np.array(list(row)).astype(np.float64)
 
with handleoutxopt as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabxopt = np.array(list(row)).astype(np.float64)

'''
inabsolutesubtract = np.subtract(inlabxopt, inlabxact)
inabsoluteerror = np.abs(inabsolutesubtract)
inlabxoptabs = np.abs(inlabxopt)
inxrelativeerror = np.true_divide(inabsoluteerror, inlabxoptabs)

outabsolutesubtract = np.subtract(outlabxopt, outlabxact)
outabsoluteerror = np.abs(outabsolutesubtract)
outlabxoptabs = np.abs(outlabxopt)
outxrelativeerror = np.true_divide(outabsoluteerror, outlabxoptabs)


with handleinyact as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inlabyact = np.array(list(row)).astype(np.float64)

with handleinyopt as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inlabyopt = np.array(list(row)).astype(np.float64)

with handleoutyact as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabyact = np.array(list(row)).astype(np.float64)
 
with handleoutyopt as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabyopt = np.array(list(row)).astype(np.float64)

inabsolutesubtract = np.subtract(inlabyopt, inlabyact)
inabsoluteerror = np.abs(inabsolutesubtract)
inlabyoptabs = np.abs(inlabyopt)
inyrelativeerror = np.true_divide(inabsoluteerror, inlabyoptabs)

outabsolutesubtract = np.subtract(outlabyopt, outlabyact)
outabsoluteerror = np.abs(outabsolutesubtract)
outlabyoptabs = np.abs(outlabyopt)
outyrelativeerror = np.true_divide(outabsoluteerror, outlabyoptabs)


n = scipy.stats.ttest_ind(outlabeff, inlabeff, equal_var=False)
print "t-statistic is %.10f and the p-value is %.75f." % n


n = scipy.stats.ttest_ind(outlabtimes, inlabtimes, equal_var=False)
print "t-statistic is %.10f and the p-value is %.300f." % n


n = scipy.stats.ttest_ind(outlabspeeds, inlabspeeds, equal_var=False)
print "t-statistic is %.10f and the p-value is %.10f." % n


n = scipy.stats.ttest_ind(inovershoot, outovershoot, equal_var=False)
print "t-statistic is %.10f and the p-value is %.300f." % n


n = scipy.stats.ttest_ind(inyrelativeerror, outyrelativeerror, equal_var=False)
print "t-statistic is %.10f and the p-value is %.25f." % n

#print inhovertime
#print outhovertime

varianceineff = np.var(inlabeff)
varianceouteff = np.var(outlabeff)
varianceintime = np.var(inlabtimes)
varianceouttime = np.var(outlabtimes)
varianceinspeed = np.var(inlabspeeds)
varianceoutspeed = np.var(outlabspeeds)


print "In lab eff var " + str(varianceineff)
print "Out lab eff var " + str(varianceouteff)
print "in lab time var " + str(varianceintime)
print "out lab time var " + str(varianceouttime)
print "in lab speed var " + str(varianceinspeed)
print "out lab speed var " + str(varianceoutspeed)

print np.median(inlabeff)
print np.median(inlabspeeds)
print np.median(inlabtimes)
print np.median(outlabeff)
print np.median(outlabspeeds)
print np.median(outlabtimes)

efftest = scipy.stats.ttest_ind(inlabeff, outlabeff, equal_var=True)
timetest = scipy.stats.ttest_ind(outlabtimes, inlabtimes, equal_var=True)
speedtest = scipy.stats.ttest_ind(inlabspeeds, outlabspeeds, equal_var=False)

print "Efficiency: t-statistic is %.10f and the p-value is %.100f." % efftest
print "Time: t-statistic is %.10f and the p-value is %.800f." % timetest
print "Speed: t-statistic is %.10f and the p-value is %.60f." % speedtest


print scipy.stats.ttest_ind(varianceouteff, varianceineff, equal_var=True)
print scipy.stats.ttest_ind(varianceouttime, varianceintime, equal_var=True)
print scipy.stats.ttest_ind(varianceoutspeed, varianceinspeed, equal_var=False)

#print inlabtimes[1] - inlabtimes[0]
#print outlabtimes[0] - outlabtimes[1]

#n = scipy.stats.mannwhitneyu(inlabspeeds, outlabspeeds, alternative='greater')
#print "t-statistic is %.10f and the p-value is %.60f." % n

#print "In variance: " + np.var(inlabeff)
#print "Out variance: " + np.var(outlabeff)
'''

print len(inlabeff) + len(outlabeff) -1
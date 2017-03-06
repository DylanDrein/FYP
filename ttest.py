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

handle5 = open("./Metricstest/inlabspeed.csv", 'rb')
handle6 = open("./Metricstest/outlabspeed.csv", 'rb')

inlabeff = []
outlabeff = []
inlabtimes = []
outlabtimes = []
inlabspeeds = []
outlabspeeds = []


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


with handle5 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inlabspeeds = np.array(list(row)).astype(np.float32)

with handle6 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabspeeds = np.array(list(row)).astype(np.float32)

#n = scipy.stats.ranksums(inlabeff, outlabeff)
#n = scipy.stats.mannwhitneyu(outlabeff, inlabeff, alternative='greater')
#print "t-statistic is %.10f and the p-value is %.60f." % n

'''
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
'''

print np.median(inlabeff)
print np.median(inlabspeeds)
print np.median(inlabtimes)
print np.median(outlabeff)
print np.median(outlabspeeds)
print np.median(outlabtimes)


'''
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
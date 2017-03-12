import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

#handle1 = open("./metricstest/outlabtimes.csv", 'rb')

handle1 = open("./metricstest/outlabeff.csv", 'rb')
handle2 = open("./metricstest/inlabeff.csv", 'rb')

with handle1 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		print len(row)

with handle2 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		print len(row)
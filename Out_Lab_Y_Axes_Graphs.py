import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

handle1 = open("./metricstest/outlabyactual.csv", 'rb')
handle2 = open("./metricstest/outlabyoptimal.csv", 'rb')

outlabyact = []
outlabyopt = []

with handle1 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabyact.append(np.array(list(row)).astype(np.float))

with handle2 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabyopt.append(np.array(list(row)).astype(np.float))
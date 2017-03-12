import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

handle1 = open("./metricstest/inlabyactual.csv", 'rb')
handle2 = open("./metricstest/inlabyoptimal.csv", 'rb')

inlabyact = []
inlabyopt = []

with handle1 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inlabyact.append(np.array(list(row)).astype(np.float))

with handle2 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inlabyopt.append(np.array(list(row)).astype(np.float))
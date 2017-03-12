import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

handle1 = open("./metricstest/outlabxactual.csv", 'rb')
handle2 = open("./metricstest/outlabxoptimal.csv", 'rb')

outlabxact = []
outlabxopt = []

with handle1 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabxact.append(np.array(list(row)).astype(np.float))

with handle2 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabxopt.append(np.array(list(row)).astype(np.float))
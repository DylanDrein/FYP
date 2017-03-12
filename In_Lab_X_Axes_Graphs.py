import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

handle1 = open("./metricstest/inlabxactual.csv", 'rb')
handle2 = open("./metricstest/inlabxoptimal.csv", 'rb')

inlabxact = []
inlabxopt = []

with handle1 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inlabxact.append(np.array(list(row)).astype(np.float))

with handle2 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inlabxopt.append(np.array(list(row)).astype(np.float))
import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

handle1 = open("./metricstest/inlabyactual.csv", 'rb')
handle2 = open("./metricstest/inlabyoptimal.csv", 'rb')

with handle1 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		print len(row)

with handle2 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		print len(row)
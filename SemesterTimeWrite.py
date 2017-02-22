'''
CSV FORMAT

Anthony Coleman	1.42021E+12	137	375	mouseDown
[      0             1       2   3     4]
      Name			time 	 y   x    type
'''


import json
import csv
import os
import numpy as np


handle = open("./AllMouseDownEvents/MouseClicktimes.csv", 'wb')

filenum = 0

times = []

rootdir = "./CSVSeparated/"

parsed = ""

for current_directory, directories, files in os.walk(rootdir):
	
	for file in files:
		filenum += 1
		filepath = os.path.join(current_directory,file)
		
		with open(filepath) as infile:
			
			parsed=csv.reader(infile)
			for row in parsed:

				if(row[4] == "mouseDown"):
					times.append(float(row[1]))
					#print type(row[1])

		print filenum

c = csv.writer(handle, delimiter = ',')
times.sort()
c.writerow(sort(list(times)))
'''
CSV FORMAT

Anthony Coleman 1.42021E+12 137 375 mouseDown
[      0             1       2   3     4]
      Name          time     y   x    type
'''

import json
import csv
import os
import numpy as np


handle1 = open("./LabDayMouseEvents/lab1.csv", 'wb')
handle2 = open("./LabDayMouseEvents/lab2.csv", 'wb')

filepath = "./AllMouseDownEvents/MouseClicktimes.csv"

lab1times = []
lab2times = []

firstlabmidnight = 1415318400000 # 7th of november
secondlabmidnight = 1417132800000 # 28th of november
daymilliseconds = 86400000

        
with open(filepath) as infile:
    parsed=csv.reader(infile)
    for row in parsed:
        for pos in row:
            #print pos
            if(float(pos) > firstlabmidnight and float(pos) < firstlabmidnight + daymilliseconds):
                lab1times.append(pos)
            if(float(pos) > secondlabmidnight and float(pos) < secondlabmidnight + daymilliseconds):
                lab2times.append(pos)

#print lab1times
#print lab2times

c1 = csv.writer(handle1, delimiter = ',')
c2 = csv.writer(handle2, delimiter = ',')

c1.writerow(lab1times)
c2.writerow(lab2times)
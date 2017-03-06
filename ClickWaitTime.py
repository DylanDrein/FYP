'''
A script which measures the time a user rests the mouse on the target before clicking
'''

import os, sys
import json
import numpy as np
import csv

rootdir = './CSVSeparated/'

check = False

fileHandles = {}
count = 0
filenum = 0
lastName=None

initialTime = 0
initialx = 0
initialy = 0
hoverx = 0
hovery = 0

lab1start = 1415358000000 # 11am 7th november
lab1end = 1415365200000 # 1pm

lab2start = 1417172400000 # 11am 28th of november
lab2end = 1417179600000 # 1pm

clickTime = 0
hoverTime = 0

hovertimesinlab = []
hovertimesoutlab = []

totalhovertimesinlab = []
totalhovertimesoutlab = []

fileHandles={}

lastName=None
handle=None

hovertimesarray = []

'''
CSV FORMAT

Anthony Coleman	1.42021E+12	137	375	mouseDown
[      0             1       2   3     4]
      Name			time 	 y   x    type
'''

for current_directory, directories, files in os.walk(rootdir):
	
	for file in files:
		filenum += 1
		filepath = os.path.join(current_directory,file)
	

		with open(filepath) as infile:
			parsed = csv.reader(infile)

			for row in parsed:
		
				name = row[0]

				'''
				##ONLY USED TO GENERATE INDIVIDUAL USER FILES##
				if(lastName!=name):
					if name in fileHandles:
					    handle=fileHandles[name]
					else:
					    #this is the first time we are seeing this name. If a corresponding file already exists, delete it.
					    filename= "./ClickWaitTimes/" + name.lower().replace(" ","-") + "-wait.csv"
					    handle=fileHandles[name]=open(filename, 'wb')
				'''

				#IN LAB
				if( ((float(row[1]) > lab1start) and (float(row[1]) < lab1end)) or ((float(row[1]) > lab2start) and (float(row[1]) < lab2end)) ):
					
					if(check == True and row[3] == initialx and row[2] == initialy):
						clickTime = float(row[1])
						hoverTime = initialTime - clickTime
						totalhovertimesinlab.append(hoverTime)
						hoverTime = 0
						clickTime = 0
						check = False
					
					if(row[4] == "mouseDown"):
						check = True
						initialTime = float(row[1])
						initialx = row[3]
						initialy = row[2]
						hoverTime = 0
						clickTime = 0

				else:
					if(check == True and row[3] == initialx and row[2] == initialy):
						clickTime = float(row[1])
						hoverTime = initialTime - clickTime
						totalhovertimesoutlab.append(hoverTime)
						hoverTime = 0
						clickTime = 0
						check = False
					
					if(row[4] == "mouseDown"):
						check = True
						initialTime = float(row[1])
						initialx = row[3]
						initialy = row[2]
						hoverTime = 0
						clickTime = 0

			c = csv.writer(handle, delimiter = ',')
			
			c.writerow(hovertimesarray)

			hoverTime = 0
			initialTime = 0
			clickTime = 0
			initialx = 0
			initialy = 0
			check = False
			hovertimesarray = []

			print filenum
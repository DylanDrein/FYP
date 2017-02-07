import json
import csv
import os

#dictionary to keep track of files we have written to so far
fileHandles={}

count=0

lastName=None
handle=None

filenum = 0

rootdir = "./UsersReversed/"

for current_directory, directories, files in os.walk(rootdir):
	
	for file in files:
		filenum += 1
		filepath = os.path.join(current_directory,file)
		
		with open(filepath) as infile:
			for line in infile:
				count+=1
				parsed=json.loads(line)

				name=parsed['name']

				#only change filehandle if lastName is different to this name
				if(lastName!=name):
					if name in fileHandles:
					    handle=fileHandles[name]
					else:
					    #this is the first time we are seeing this name. If a corresponding file already exists, delete it.
					    filename= "./CSVSeparated/" + name.lower().replace(" ","-")+".csv"
					    handle=fileHandles[name]=open(filename, 'wb')

				del parsed['cX']
				del parsed['cY']

				c = csv.writer(handle, delimiter = ',')
				
				c.writerow([parsed['name'], parsed['time'], parsed['y'], parsed['x'], parsed['type']])
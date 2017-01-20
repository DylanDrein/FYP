import os
from operator import itemgetter, attrgetter, methodcaller
import json
from collections import OrderedDict


rootdir = './Userss'
reversedpath = './UsersReversed'

def rawcount(filename):
	filenamejoin = os.path.join(rootdir, filename)
	f = open(filenamejoin, 'rb')
	lines = 0
	buf_size = 1024 * 1024
	read_f = f.read

	buf = read_f(buf_size)
	while buf:
		lines += buf.count('\n')
		buf = read_f(buf_size)
   
	return lines

fileHandles = {}
count = 0
totalfilelines = 0
filenum = 0
lastName=None
handle=None

for current_directory, directories, files in os.walk(rootdir):
	#print files
	#print "---------"
	#print len(files)
	for file in files:
		#print file
		filenum += 1
		filepath = os.path.join(current_directory,file)
		#print fullname + "2"
		with open(filepath) as infile:
			#infilesorted = sorted(infile, key = attrgetter('time'), reverse = True)
			#print infile
			for line in reversed(list(infile)):
			#for line in infile:
				#print line
				count += 1
				parsed = json.loads(line)
				#print parsed
				
				name = parsed['name']
				#print name
				
				if(lastName != name):
					if name in fileHandles:
						handle = fileHandles[name]
					else:
						filename = name.lower().replace(" ", "-") + "-reversed.json"
						finalname = os.path.join(reversedpath, filename)
						totalfilelines = rawcount(file)
						handle = fileHandles[name] = open(finalname, 'w')

				handle.write(json.dumps(parsed)+"\n")
				
				if(count%100000==0):
					print "File #" + str(filenum)
		        	print "{0:.2f}".format(count/(totalfilelines/10))+"% complete"
		        
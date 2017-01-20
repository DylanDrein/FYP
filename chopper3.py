import json

#dictionary to keep track of files we have written to so far
fileHandles={}

count=0


lastName=None
handle=None

with open("mousecopy.json") as infile:
    for line in infile:
        count+=1
        parsed=json.loads(line)
        #filter out click events (mouseDown and mouseUp are retained)
        if parsed["type"]=="click": continue

        name=parsed['name']

        #only change filehandle if lastName is different to this name
        if(lastName!=name):
		if name in fileHandles:
		    handle=fileHandles[name]
		else:
		    #this is the first time we are seeing this name. If a corresponding file already exists, delete it.
		    filename=name.lower().replace(" ","-")+".json"
		    handle=fileHandles[name]=open(filename, 'w')


        #filter out a few fields if they are present
        #assert("tabid" in parsed)
        del parsed["tabid"]
        del parsed["sessid"]
        del parsed["version"]


        #delete the type field - but do it in a paranoid way
        if(parsed["type"]=="mousemove"):
        #   assert(parsed["event"]=="mouse move")
            del parsed["event"]
        elif(parsed["type"]=="mouseDown"):
        #   assert(parsed["event"]=="mouse down")
            del parsed["event"]
        elif(parsed["type"]=="mouseUp"):
        #   assert(parsed["event"]=="mouse up")
            del parsed["event"]

        
        handle.write(json.dumps(parsed)+"\n")

        if(count%100000==0):
            print "{0:.2f}".format((count/885576.50))+"% complete"

        lastName=name
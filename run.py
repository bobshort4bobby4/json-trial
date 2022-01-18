import json

var datafile = "5line-horsepro.json"

horsedata = []

def loaddata(datafile):
    """
    A function to load a json file into a variable
    """
    print("Please hold your horses!!.....loading data can take 20 seconds thanks")
    for line in open(datafile,"r"):
        #line = line.replace('None', "null")
        horsedata.append(json.loads(line))

loaddata(datafile)
print(horsedata[0])
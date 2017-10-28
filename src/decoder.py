import csv

#Reads a csv file into a list of tuples
def getBirths(fileName):
    with open(fileName, 'r') as csvfile:
        lines = []
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            lines.append(','.join(row))
        return lines

#returns a list of tuples with the name and the amount of times the name has been used.
def getTotals(births):
    totals = {}
    for b in births:
        num = int(b.split(',')[3])
        name = b.split(',')[1]
        if(name in totals):
            totals[name] = totals[name] + num
        else:
            totals[name] = num
    return totals

#wirtes the data to the file "filename" data should be a list
def writeToFile(data, filename):
    f = open(filename,"w+")
    for d in data:
            f.write("{}\n".format(d))
    f.close()


births = getBirths('ssa-births.csv')
totals = getTotals(births)
print(totals['Marry'])
popularNames = sortByPopular(births)

#returns the name minus "splitPoint" characters
def getLeft(name, splitPoint):
    return name[:splitPoint]

#returns the name minus the first "splitPoint"
def getRight(name, splitPoint):
    return name[splitPoint:]
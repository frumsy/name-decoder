import csv
import numpy as np

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

births = getBirths('../res/births-post-1914.csv')
#totals = getTotals(births)
#print(totals['Marry'])
#popularNames = sortByPopular(births)
    
#returns the name minus "splitPoint" characters
def getLeft(name, splitPoint):
    return name[:splitPoint]

#returns the name minus the first "splitPoint"
def getRight(name, splitPoint):
    return name[splitPoint:]




#clean data::::

#filter out per year
def dataAfter(data, year):
    dataAfter = []
    for d in data:
        curYear = int(d.split(',')[0])#year
        if(year < curYear):#add to new list:
            dataAfter.append(d)
    return dataAfter

def dataBefore(data, year):
    dataBefore = []
    for d in data:
        curYear = int(d.split(',')[0])#year
        if(year > curYear):#add to new list:
            dataBefore.append(d)
    return dataBefore

def dataIn(data, year):
    dataIn = []
    for d in data:
        curYear = int(d.split(',')[0])#year
        if(year == curYear):#add to new list:
            dataIn.append(d)
    return dataIn

#get total number of births from data given:
def totalBirths(data):
    total = 0
    for d in data:
        total += int(d.split(',')[3])#number births
    return total

def totalToFreq(data,fromYear, toYear):
    #make map of year to total number of births in that year
    yearToBirth = {}
    for i in range(fromYear,toYear+1):
        yearToBirth[i] = totalBirths(dataIn(data, i))
    #new list of string to write to file
    lines = []

    for d in data:
        curYear = int(d.split(',')[0])#year of the line
        if(fromYear <= int(d.split(',')[0]) and toYear >= curYear):
            name = d.split(',')[1]#name of the line
            sex = d.split(',')[2]#sex of the line
            amount = int(d.split(',')[3])#number of births for the line
            freq = amount/yearToBirth[curYear]#freq of births for the line
            lines.append(str(curYear) + ',' + name + ',' + sex + ',' + str(freq))
    return lines

#given filename, return a dict of 4 nparrays - year, name, gender, freq
def getNumpyArrays(filename='../res/testbirths.csv'):
    temparry = ([], [], [], [])
    with open(filename) as f:
        for line in f:
            vals = line.strip().split(',')
            for arry, val in zip(temparry, vals):
                arry.append(val)
    return {'year' : np.array(temparry[0]), 'name' : np.array(temparry[1]), 'gender' : np.array(temparry[2]), 'freq' : np.array(temparry[3])}

#returns an int version of a string based purely on concatenated ascii value
def stoint(string):
    return int(reduce(lambda i, c: i+str(ord(c)), string, ''))

    #end cleaning functions

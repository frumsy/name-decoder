import csv
import numpy as np

combinedName = ""
splitPoint = 0

def getSplit():
    return 4

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

def sortByPopular(births):
    print(births[0])
    print(births[0].split(',')[3])

    return []

def writeToFile(data, filename):
    f = open(filename,"w+")
    for d in data:
            f.write("{}\n".format(d))
    f.close()

births = getBirths('ssa-births.csv')
totals = getTotals(births)
print(totals['Marry'])
popularNames = sortByPopular(births)

def getLeft(splitPoint):
    return combinedName[:splitPoint]

def getRight(splitPoint):
    return combinedName[splitPoint:]


#given filename, return a dict of 4 nparrays - year, name, gender, freq
def getNumpyArrays(filename='../res/testbirths.csv'):
    temparry = ([], [], [], [])
    with open(filename) as f:
        for line in f:
            vals = line.strip().split(',')
            for arry, val in zip(temparry, vals):
                arry.append(val)
    return {'year' : np.array(temparry[0]), 'name' : np.array(temparry[1]), 'gender' : np.array(temparry[2]), 'freq' : np.array(temparry[3])}


"""
import edu.umass.cs.CSV
import PathImplicits._
import java.io.File
import java.nio.file.Path
import java.nio.file.Paths

object CoupleDecoder{

val births = CSV.fromFile("ssa-births.csv")//births
val CDC = CSV.fromFile("cdc-life-expectancy.csv")//life expectancy
val girls = CSV.fromFile("girls-names.txt").flatten//names of girls
val boys = CSV.fromFile("boys-names.txt").flatten//names of boys
val locationData = CSV.fromFile("location.csv")
val tlocation = CSV.fromFile("testlocation.csv")
//val girls = births.filter((record: List[String]) => record(2) == "F").map(x=> x(1))//.flatten
//val boys = births.filter((record: List[String]) => record(2) == "M").map(x=> x(1))//.flatten
val t = "jathian"

def onlyName(data: List[List[String]], name: String ): List[List[String ]] =
{
	data.filter((record: List[String]) => record(1) == name)
}



//returns a tuple with the the most popular name and then the number of times it has occured.
def mostPopular(data: List[List[String ]]): (String , Int) =
{
	val ls = data.map(x => x(1) -> x(3).toInt)
	//println("1: " + ls)
	val groupedMap = ls.groupBy(x => x._1)
	//println("2:" + groupedMap)
	val mapLstInts = groupedMap.map(x => x._1 -> x._2.map(y => y._2) )//convert to (string,int)
	//println("3: " + mapLstInts)
	val totals = mapLstInts.map(x => x._1 -> x._2.fold(0)( (a,i) => a + i.toInt ) )
	//println("4: " + totals)
	val t = totals.maxBy(i => i._2)
	//println(t)
	t
}

// def getPop(input: List[String]): (String , Int) =
// {
// 	val input.map(x=>onlyName(births,x)).flatten
// }

//writes every element of the list to a new line in the txt file given.
def writeLines(file: Path, data: List[String])
{
val toWrite = data.map(x=>x.toString + "\n")
file.write(toWrite.mkString)
}

def count(data: List[List[String ]]): Int =
{
	val nums = data.map(x => x(3).toInt)
	nums.fold(0)( (a,i) => a + i )
}

//returns the number of girls and boys born for the list given to te function.
def countGirlsAndBoys(data: List[List[String ]]): (Int , Int) =
{
	val numG = data.filter((record: List[String]) => record(2) == "F")
	val numB = data.filter((record: List[String]) => record(2) == "M")
	(count(numG), count(numB))
}

//Helper function for genderNeutralNames
def duplicateName(s: String, lst: Set[(String,String)]): Boolean =
{
	lst.filter(x => x._1 == s).size > 1
}

//returns a set of strings containing gender neutral names
def genderNeutralNames(data: List[List[String ]]): Set[String] =
{
	val s = data.map(x => (x(1)-> x(2))).toSet
	//println("1: " + s)
	val gnn = s.filter(x => duplicateName(x._1, s))
	//println("2: " + gnn)
	gnn.map(x=> x._1)
}

}//End decoder
"""

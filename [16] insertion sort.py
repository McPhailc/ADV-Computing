rows = 58
cols = 4

def initialise():
    array = [[None]*cols for index in range(rows)]
    return array

def readFile(array,filePath):
    with open(filePath) as readfile:
        r = 0
        line = readfile.readline().rstrip('\n')
        while line:
            items = line.split(",")
            for c in range(cols):
                array[r][c] = items[c]
            r += 1
            line = readfile.readline().rstrip('\n')
    return array

def insertionSort(array):
    for i in range(1,len(array)):
        value1 = int(array[i][0])
        value2 = array[i][1]
        value3 = array[i][2]
        value4 = array[i][3]
        index = i
        while (index > 0) and (value1 < int(array[index-1][0])):
            array[index][0] = array[index-1][0]
            array[index][1] = array[index-1][1]
            array[index][2] = array[index-1][2]
            array[index][3] = array[index-1][3]
            index -= 1
        array[index][0] = value1
        array[index][1] = value2
        array[index][2] = value3
        array[index][3] = value4       
    return array

def printData(array):
    for index in range(len(array)):
        print("Super Bowl " + array[index][1] + " - " + array[index][2])

# MAIN #
superBowl = initialise()
superBowl = readFile(superBowl,"Data Files/superBowl.txt")
superBowl = insertionSort(superBowl)
printData(superBowl)

rows = 100
cols = 3

def readFile(filePath):
    array = [[None]*cols for index in range(rows)]
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

def bubbleSort(array):
    length = rows
    swapped = True
    while (length >= 0) and (swapped == True):
        swapped = False
        for r in range(length-1):
            if int(array[r][1]) < int(array[r+1][1]):
                array[r], array[r+1] = array[r+1], array[r]
            swapped = True
        length -= 1
    return array

def printData(array):
    for index in range(rows):
        if (int(array[index][1]) >= 1000000000) and  (int(array[index][2])%2 == 1):
            print("$", array[index][1], array[index][2], array[index][0])

# MAIN #
movie = readFile("Data Files/movies.csv")
movie = bubbleSort(movie)
printData(movie)

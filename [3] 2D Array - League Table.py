rows = 21
cols = 9

def readFile(filePath):
    array = [[None]*cols for i in range(rows)]
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

def calculate(array):
    for r in range(1, rows):
        array[r][7] = int(array[r][5]) - int(array[r][6])
        array[r][8] = int(array[r][2])*3 + int(array[r][3])
    return array

def printData(array):
    rowText = "\n"
    for r in range(rows):
        for c in range(cols):
            rowText += str(array[r][c]) + " "
        print(rowText)
        rowText = ""

# MAIN #
league = readFile("Data Files/league.txt")
league = calculate(league)
printData(league)

##def calculate2(array):
##    for r in range(1, rows):
##        array[r][7] = int(array[r][5]) - int(array[r][6])
##        if (array[r][7] >= 0) and (array[r][7] <= 9):
##            array[r][7] = "  " + str(array[r][7])
##        elif array[r][7] >= 10:
##            array[r][7] = " " + str(array[r][7])
##        array[r][8] = (int(array[r][2])*3) + (int(array[r][3]))
##    return array
##
##def printData2(array):
##    print("")
##    for r in range(rows):
##        print("%-21s %-3s %-3s %-3s %-3s %-3s %-2s %-4s %2s" %(array[r][0], array[r][1], array[r][2], array[r][3], array[r][4], array[r][5], array[r][6], array[r][7], array[r][8]))


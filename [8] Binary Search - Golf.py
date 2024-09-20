rows = 233
cols = 5

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

def binarySearch(array,target):
    low = 0
    high = len(array)-1
    found = False
    while (found == False) and (low <= high):
        mid = (low + high) // 2
        if target == array[mid][0]:
            found = True
        elif target > array[mid][0]:
            low = mid + 1
        else:
            high = mid - 1
    return found,mid

def printData(array,found,mid):
    if found == True:
        total = int(array[mid][1]) + int(array[mid][2]) + int(array[mid][3]) + int(array[mid][4])
        print("\nName: " + array[mid][0])
        print("Number of major championships won: " + str(total))
    else:
        print("Golfer not found")

# MAIN #
golfer = readFile("Data Files/golf.csv")
target = input("What golfer are you searching for? ")
found, pos = binarySearch(golfer,target)
printData(golfer,found,pos)

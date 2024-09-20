class countryRecord():
    name = ""
    capital = ""

def readFile(filePath):
    asia = [countryRecord() for i in range(50)]
    with open(filePath) as readfile:
        index = 0
        line = readfile.readline().rstrip('\n')
        while line:
            items = line.split(",")
            asia[index].name = items[0]
            asia[index].capital = items[1]
            line = readfile.readline().rstrip('\n')
            index += 1
    return asia

def binarySearch(asia,target):
    low = 0
    high = len(asia)-1
    found = False
    while (found == False) and (low <= high):
        mid = (low + high) // 2
        if target == asia[mid].name:
            found = True
        elif target > asia[mid].name:
            low = mid + 1
        else:
            high = mid - 1
    if found == True:
        print("Position: " + str(mid))
        print("Capital:  " + asia[mid].capital)
    else:
        print(target + " not found")


# MAIN #
asia = readFile("Data Files/asia.txt")
target = input("What country are you searching for? ")
binarySearch(asia,target)

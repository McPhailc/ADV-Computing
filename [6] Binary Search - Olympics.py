def readFile(filePath):
    city = [""] * 30
    country = [""] * 30
    year = [0] * 30
    with open(filePath) as readfile:
        index = 0
        line = readfile.readline().rstrip('\n')
        while line:
            items = line.split(",")
            city[index] = items[0]
            country[index] = items[1]
            year[index] = int(items[2])
            line = readfile.readline().rstrip('\n')
            index += 1
    return city, country, year

def binarySearch(city,country,year,target):
    low = 0
    high = len(city)-1
    found = False
    while (found == False) and (low <= high):
        mid = (low + high)//2
        if target == year[mid]:
            found = True
        elif target > year[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if found == True:
        print("The " + str(target) + " Summer Olympic Games were held in:")
        print(city[mid] + ", " + country[mid])
    else:
        print(str(target) + " not found")


# MAIN #
city,country,year = readFile("Data Files/olympics.txt")
target = int(input("What year are you searching for? "))
binarySearch(city,country,year,target)

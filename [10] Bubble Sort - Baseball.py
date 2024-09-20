def readFile(filePath):
    team = [""]*30
    wsWins = [0]*30
    stadium = [""]*30
    capacity = [0]*30
    with open(filePath) as readfile:
        index = 0
        line = readfile.readline().rstrip('\n')
        while line:
            items = line.split(",")
            team[index] = items[0]
            wsWins[index] = int(items[1])
            stadium[index] = items[2]
            capacity[index] = int(items[3])           
            index += 1
            line = readfile.readline().rstrip('\n')
    return team,wsWins,stadium,capacity

def sortStadiums(stadium,capacity):
    length = len(stadium)
    swapped = True
    while (length >= 0) and (swapped == True):
        swapped = False
        for index in range(length-1):
            if capacity[index] < capacity[index+1]:
                stadium[index],stadium[index+1] = stadium[index+1],stadium[index]
                capacity[index],capacity[index+1] = capacity[index+1],capacity[index]              
                swapped = True
        length -= 1
    print("Stadiums sorted by capacity")
    for index in range(len(stadium)):
        print(capacity[index], stadium[index])

def sortWorldSeriesWins(team,wsWins):
    length = len(team)
    swapped = True
    while (length >= 0) and (swapped == True):
        swapped = False
        for index in range(length-1):
            if wsWins[index] < wsWins[index+1]:
                team[index],team[index+1] = team[index+1],team[index]
                wsWins[index],wsWins[index+1] = wsWins[index+1],wsWins[index]
                swapped = True
        length -= 1
    print("\nTeams sorted by World Series wins")
    for index in range(len(team)):
        print(wsWins[index], team[index])

# MAIN #
team,wsWins,stadium,capacity = readFile("Data Files/baseball.txt")
sortStadiums(stadium,capacity)
sortWorldSeriesWins(team,wsWins)



























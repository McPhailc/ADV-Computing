class playerRecord():
    name = ""
    points = 0
    games = 0
    ppg = 0.0

def readFile(filePath):
    player = [playerRecord() for i in range(50)]
    with open(filePath) as readfile:
        index = 0
        line = readfile.readline().rstrip('\n')
        while line:
            items = line.split(",")
            player[index].name = items[0]
            player[index].points = int(items[1])
            player[index].games = int(items[2])
            index += 1
            line = readfile.readline().rstrip('\n')
    return player

def calculateAverage(player):
    for index in range(len(player)):
        player[index].ppg = round(player[index].points/player[index].games,1)
    return player

def sortAverage(player):
    length = len(player)
    swapped = True
    while (length >= 0) and (swapped == True):
        swapped = False
        for index in range(length-1):
            if player[index].ppg < player[index+1].ppg:
                player[index], player[index+1] = player[index+1], player[index]
            swapped = True
        length -= 1
    print("\nPlayers sorted by average ppg")
    printData(player)

def sortPoints(player):
    length = len(player)
    swapped = True
    while (length >= 0) and (swapped == True):
        swapped = False
        for index in range(length-1):
            if player[index].points < player[index+1].points:
                player[index], player[index+1] = player[index+1], player[index]
            swapped = True
        length -= 1
    print("\nPlayers sorted by total points")
    printData(player)

def printData(player):
    for index in range(len(player)):
        print(player[index].ppg, player[index].points, player[index].name)

# MAIN #
player = readFile("Data Files/basketball.csv")
player = calculateAverage(player)
sortAverage(player)
sortPoints(player)

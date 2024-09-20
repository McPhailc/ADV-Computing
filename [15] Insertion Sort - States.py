class record():
    capital = ""
    name = ""
    abbreviation = ""

def readFile(filePath):
    state = [record() for index in range(50)]
    with open(filePath) as readfile:
        index = 0
        line = readfile.readline().rstrip('\n')
        while line:
            items = line.split(",")
            state[index].capital = items[0]
            state[index].name = items[1]
            state[index].abbreviation = items[2]
            line = readfile.readline().rstrip('\n')
            index += 1
    return state

def insertionSort(state):
    for i in range(1,len(state)):
        value1 = state[i].capital
        value2 = state[i].name
        value3 = state[i].abbreviation
        index = i
        while (index > 0) and (value2 < state[index-1].name):
            state[index].capital = state[index-1].capital
            state[index].name = state[index-1].name
            state[index].abbreviation = state[index-1].abbreviation
            index -= 1
        state[index].capital = value1
        state[index].name = value2
        state[index].abbreviation = value3
    return state

def printData(state):
    for index in range(len(state)):
        print(state[index].abbreviation, state[index].name)

# MAIN #
state = readFile("Data Files/states.txt")
state = insertionSort(state)
printData(state)

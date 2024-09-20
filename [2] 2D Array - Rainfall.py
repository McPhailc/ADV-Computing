rows = 52
cols = 7

def readFile(filePath):
    array = [[None]*cols for i in range(rows)]
    # Open the external file
    with open(filePath) as readfile:
        # Initialise the row counter
        r = 0
        # Store the data in the current line of the file
        line = readfile.readline().rstrip('\n')
        # Loop while there are still lines of data
        while line:
            # Split the line of data up and store
            # the data into an array called 'items'
            items = line.split(",")
            # Loop across the columns in the current row
            for c in range(cols):
                # Store each piece of data into the array
                array[r][c] = int(items[c])
            # Increment the row counter
            r += 1
            # Read and store the next line to be used
            line = readfile.readline().rstrip('\n')
    return array

def yearly(array):
    # Initialise running total
    yearTotal = 0
    # Traverse the array's rows and columns
    for r in range(rows):
        for c in range(cols):
            # Add the current value to the total   
            yearTotal += array[r][c]
    # Output the final total and a return carriage
    print("Yearly total: " + str(yearTotal) + "\n")

def weekly(array):
    print("Week  " + "Average " + "Min  " + "Max")
    for r in range(rows):
        total = 0
        weekMin = 999
        weekMax = 0
        for c in range(cols):
            total += array[r][c]
            if array[r][c] < weekMin:
                weekMin = array[r][c]
            if array[r][c] > weekMax:
                weekMax = array[r][c]
        weekAverage = round(total/7,1)
        if r < 9:
            print(" " + str(r+1) + "    " + str(weekAverage) + "    " + str(weekMin) + "    " + str(weekMax))
        else:
            print(str(r+1) + "    " + str(weekAverage) + "    " + str(weekMin) + "    " + str(weekMax))

# MAIN #
rainfall = readFile("Data Files/rainfall.csv")
yearly(rainfall)
weekly(rainfall)



























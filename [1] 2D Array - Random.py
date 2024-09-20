# Import the random library
import random

# Initialise variables with row and column sizes
rows = 4
cols = 5

def fillArray():
    # Initialise an empty 2D array    
    array = [[None]*cols for i in range(rows)]
    # Outer loop through each row
    for r in range(rows):
        # Inner loop through each column of the row
        for c in range(cols):
            # Assign a random number into the 2D array
            array[r][c] = random.randint(0,9)
    return array

def printData(array):
    for r in range(rows):
        # Initialise rowText to store each row's contents
        rowText = ""
        for c in range(cols):
            # Concatenate array value onto rowText
            rowText += str(array[r][c]) + " "
        # Output the entire row and a return carriage
        print(rowText,"\n")

# MAIN #
randomNumbers = fillArray()
printData(randomNumbers)

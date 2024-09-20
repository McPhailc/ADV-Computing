rows = 3
cols = 9
import random

def fillArray():
    array = [[None]*cols for i in range(rows)]
    # Initialise 1-D array of False values
    # that will update when new numbers are chosen
    chosenNum = [False]*91
    # Outer loop through each row
    for r in range(rows):
        # Inner loop through each column of the row
        for c in range(cols):
            # Flag set to false to enter the conditional loop
            selected = False
            # Loop until an appropriate number is chosen
            while selected == False:
                # Generate an appropriate, random number
                # column 1 = 1-10, column 2 = 2-20 etc.
                randomNum = random.randint((c*10)+1,(c+1)*10)
                # If the random number has not been chosen
                if chosenNum[randomNum] == False:
                    # Set that number as chosen so
                    # it cannot be used again
                    chosenNum[randomNum] = True
                    # Assign this number to the 2-D array
                    array[r][c] = randomNum
                    # Flag set to true to exit the loop
                    selected = True
    return array

def printData(array):
    for r in range(rows):
        # Set all columns to "not chosen"
        chosenCol = [False]*9
        # Loop to replace 4 random columns with a space
        for c in range(4):
            # Flag set to false to enter the conditional loop
            chosen = False
            # Loop until a new column has been chosen
            while chosen == False:
                # Pick a random column
                randCol = random.randint(0,8)
                # If the column has not been chosen
                if chosenCol[randCol] == False:
                    # Set that column to chosen
                    chosenCol[randCol] = True
                    # Replace the 2-D array number
                    # with a two spaces
                    array[r][randCol] = "  "
                    # Flag set to true to exit the loop
                    chosen = True
        # Output the row of numbers
        rowText = ""
        for c in range(cols):
            rowText += str(array[r][c]) + " " 
        print(rowText)

# MAIN #
ticket = fillArray()
printData(ticket)


##def fillArray2():
##    array = [[None]*cols for i in range(rows)]
##    # Initialise 1-D array of False values
##    # that will update when new numbers are chosen
##    chosenNum = [False]*91
##    # Outer loop through each row
##    for r in range(rows):
##        # Inner loop through each column of the row
##        for c in range(cols):
##            # Flag set to false to enter the conditional loop
##            selected = False
##            # Loop until an appropriate number is chosen
##            while selected == False:
##                # Generate an appropriate, random number
##                # column 1 = 1-10, column 2 = 2-20 etc.
##                randomNum = random.randint((c*10)+1,(c+1)*10)
##                # If the random number has not been chosen
##                if chosenNum[randomNum] == False:
##                    # Set that number as chosen so
##                    # it cannot be used again
##                    chosenNum[randomNum] = True
##                    # Assign this number to the 2-D array
##                    array[r][c] = randomNum
##                    # Flag set to true to exit the loop
##                    selected = True
##            if array[r][c] <= 9:
##                array[r][c] = " " + str(array[r][c])
##    return array

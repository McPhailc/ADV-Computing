import random

def fillArray():
    array = [None]*10
    for index in range(len(array)):
        array[index] = random.randint(100,999)
    return array

def bubbleSort(array):
    # Store the length of the array
    length = len(array)
    # Flag set to True to enter the conditional loop
    swapped = True
    # Loop until the array is traversed and
    # no more values need to be swapped
    while swapped == True:
        # Flag set to False and if it doesn't change
        # then the array has been sorted
        swapped = False
        # Loop to the second last array index
        for index in range(length-1):
            # If the value being check is larger than the next value
            if array[index] > array[index+1]:
                # Swap both values
                array[index], array[index+1] = array[index+1], array[index]
                # Flag set to True because a swap was made
                swapped = True
        # Decrement the length of the list because the
        # largest item was moved to the end of the array
        # and doesn't need to be check in the next iteration
        length -= 1
    return array

def printData(array):
    text = ""
    for index in range(len(array)):
        text = text + str(array[index]) + " "
    print(text)

# MAIN #
randomNumbers = fillArray()
printData(randomNumbers)
randomNumbers = bubbleSort(randomNumbers)
printData(randomNumbers)

def fillArray():
    array = [5,10,14,17,25,37,50,64,65,77]
    return array

def binarySearch(array,target):
    # Initialise low and high positions
    low = 0
    high = len(array)-1
    # Initialise the Boolean flag
    found = False
    # Loop while the target has not been found
    # and the data has not been fully searched
    while (found == False) and (low <= high):
        # Calculate the mid point of the data
        mid = (low + high)//2
        # If the target value matches the
        # value in the middle of the data
        if target == array[mid]:
            # Change the Boolean flag to True
            found = True
        # if the target value is in
        # the upper half of the data
        elif target > array[mid]:
            # Re-position and move low to
            # the upper half of the data
            low = mid + 1
        # if the target value is in
        # the lower half of the data
        else:
            # Re-position and move high to
            # the lower half of the data
            high = mid - 1

    if found == True:
        print(str(target) + " found at position " + str(mid))
    else:
        print(str(target) + " not found")

def printData(array):
    text = ""
    for index in range(len(array)):
        text = text + str(array[index]) + " "
    print(text)
        
# MAIN #
randomNumbers = fillArray()
printData(randomNumbers)
target = int(input("What number are you searching for? "))  
binarySearch(randomNumbers,target)

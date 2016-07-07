"""Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    startIndex = 0
    endIndex = len(input_array)
    
    while True:
        medianIndex = (endIndex-startIndex)/2 + startIndex
        medianVal = input_array[medianIndex]
        if value == medianVal:
            return medianIndex
        elif startIndex == medianIndex:
            return -1
        elif value > medianVal:
            startIndex = medianIndex
        elif value < medianVal:
            endIndex = medianIndex
    
    return -1

#Unresolved Bug
def binary_recursive_search(input_array, value, lowIndex, highIndex):
    if len(input_array)<=2:
        print("{} - {} / {}".format(len(input_array), lowIndex, highIndex))
        print(input_array )
        if value == input_array[0]:
            return lowIndex
        elif value == input_array[1]:
            return highIndex
        else:
            return -1
    else:
        middleIndex = (highIndex-lowIndex)/2
        middleVal = input_array[middleIndex]

        print("{}C{}  - {} / {} / {}".format(len(input_array), middleVal, lowIndex, middleIndex, highIndex))
        print(input_array )
       
        if value < middleVal:
            highIndex -= (middleIndex+1)
            return binary_recursive_search(input_array[:middleIndex], value, lowIndex, highIndex)
        elif value >= middleVal:
            lowIndex += middleIndex
            return binary_recursive_search(input_array[middleIndex:], value, lowIndex, highIndex)
        

test_list = [1,3,9,11,15,19,29,33]
test_val1 = 15
test_val2 = 15
test_val3 = 29
test_val4 = 50

print("Linear Search")
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
print binary_search(test_list, test_val3)
print binary_search(test_list, test_val4)

print("Recursive Search")
print binary_recursive_search(test_list, test_val1, 0, len(test_list)-1)
#print binary_recursive_search(test_list, test_val2, 0, len(test_list)-1)
#print binary_recursive_search(test_list, test_val3, 0, len(test_list)-1)
#print binary_recursive_search(test_list, test_val4, 0, len(test_list)-1)



"""
Quick Sort
https://www.youtube.com/watch?v=kUon6854joI

"""

def quick_sort(input_array, lowIndex, highIndex):
    if highIndex-lowIndex == 0:
        print("DR {} -> {} - {}".format(lowIndex, highIndex, input_array[lowIndex:highIndex+1]))
        return input_array
    elif highIndex-lowIndex == 1:
        if input_array[lowIndex] > input_array[highIndex]:
            tmp = input_array[highIndex]
            input_array[highIndex] = input_array[lowIndex]
            input_array[lowIndex] = tmp
        print("D1 {} -> {} - {}".format(lowIndex, highIndex, input_array[lowIndex:highIndex+1]))
        return input_array
    else:
        print("{} -> {}".format(lowIndex, highIndex))

        
        cmpIndex = lowIndex
        pivotIndex = highIndex
        pivotVal = input_array[highIndex]

        while cmpIndex != pivotIndex:
            print("{}/{}/V{} - {}".format(cmpIndex, pivotIndex, pivotVal, input_array[lowIndex:highIndex+1]))           
            if input_array[cmpIndex] > pivotVal:
                input_array[pivotIndex] = input_array[cmpIndex]
                input_array[cmpIndex] = input_array[pivotIndex-1]
                input_array[pivotIndex-1] = pivotVal
                pivotIndex -= 1
            else:
                cmpIndex += 1
            #print("{}/{}/{} - {}".format(cmpIndex, pivotIndex, pivotVal, input_array))           

        
        print("A{} -> {}".format(lowIndex, pivotIndex-1))
        print("B{} -> {}".format(pivotIndex+1, highIndex))

        if (pivotIndex < highIndex):
            quick_sort(input_array, pivotIndex+1, highIndex)
        if (lowIndex < pivotIndex):
            quick_sort(input_array, lowIndex, pivotIndex-1)


        return input_array



test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
test2 = [8,3,1,7,0,10,2,11]
print quick_sort(test, 0, len(test)-1)

"""
Quick Sort
https://www.youtube.com/watch?v=kUon6854joI

"""

def quick_sort(input_array, lowIndex, highIndex):
    if highIndex-lowIndex == 0:
        return input_array
    elif highIndex-lowIndex == 1:
        if input_array[lowIndex] > input_array[highIndex]:
            tmp = input_array[highIndex]
            input_array[highIndex] = input_array[lowIndex]
            input_array[lowIndex] = tmp
        return input_array
    else:
        cmpIndex = lowIndex
        pivotIndex = highIndex
        pivotVal = input_array[highIndex]

        while cmpIndex != pivotIndex:
            if input_array[cmpIndex] > pivotVal:
                input_array[pivotIndex] = input_array[cmpIndex]
                input_array[cmpIndex] = input_array[pivotIndex-1]
                input_array[pivotIndex-1] = pivotVal
                pivotIndex -= 1
            else:
                cmpIndex += 1      

        quick_sort(input_array, lowIndex, pivotIndex-1)
        quick_sort(input_array, pivotIndex+1, highIndex)

        return input_array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
test2 = [8,3,1,7,0,10,2]
print quick_sort(test2, 0, len(test2)-1)

"""
Bubble Sort
O(n^2)
"""

def bubble_sort(input_array, sort):

    if sort == -1:
        sortNum = len(input_array)-1
    else:
        sortNum = sort

    compIndex = len(input_array)-1
    for i in range(0,sortNum):
        for j in range(0,compIndex):
            if j != compIndex and input_array[j]>input_array[j+1]:
                tmp = input_array[j+1]
                input_array[j+1] = input_array[j]
                input_array[j] = tmp
        compIndex -= 1

    return input_array


arr = [21,4,1,3,9,20,25,6,21,14]

print(bubble_sort(arr,-1))

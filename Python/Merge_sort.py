"""
Merge Sort
O(nlog(n))
"""


def merge_sort(input_array):
    if len(input_array) == 1:
        print("{}I{}".format(1, input_array))
        return input_array
    elif len(input_array) == 2:
        if input_array[0] > input_array[1]:
            tmp = input_array[1]
            input_array[1] = input_array[0]
            input_array[0] = tmp
        print("{}I{}".format(2, input_array))
        return input_array
    else:
        halfIndex = len(input_array)/2
        A = merge_sort(input_array[:halfIndex])
        B = merge_sort(input_array[halfIndex:])

        print("{}IA{}".format(3, A))
        print("{}IB{}".format(3, B))

        aIndex = 0
        bIndex = 0
        mIndex = 0
        merged_array = [0]*(len(A) + len(B))
        while aIndex != len(A) or bIndex != len(B):
            if bIndex == len(B):
                merged_array[mIndex] = A[aIndex]
                aIndex += 1                
            elif aIndex == len(A):
                merged_array[mIndex] = B[bIndex]
                bIndex += 1
            elif A[aIndex] <= B[bIndex]:
                merged_array[mIndex] = A[aIndex]
                aIndex += 1
            elif B[bIndex] < A[aIndex]:
                merged_array[mIndex] = B[bIndex]
                bIndex += 1
            mIndex += 1
            
        return merged_array

arr = [21,4,1,3,3,9,20,25]
print(merge_sort(arr))

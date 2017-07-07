def max_contiguous(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


def max_ncontiguous(arr):
    max_num = 0
    max_negative = 0
    for x in arr:
        if x < 0:
            if max_negative == 0:
                max_negative = x
            elif x > max_negative:
                max_negative = x
        else:
            max_num += x

    if max_num == 0:
        return max_negative
    return max_num

T = int(raw_input())
for i in range(0, T):
    try:
        arr_size = int(raw_input());
        arr = [int(s) for s in raw_input().split(" ")]
        print("{} {}".format(max_contiguous(arr), max_ncontiguous(arr)))
    except EOFError:
        exit


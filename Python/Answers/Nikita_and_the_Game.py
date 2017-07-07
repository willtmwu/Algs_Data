def rec_arr_split(arr):
    if len(arr) == 1 or len(arr) == 0:
        return 0
    else:
        #find split
        split_index = -1;
        for i in xrange(0,len(arr)):
            if sum(arr[:i]) == sum(arr[i:]) :
                split_index = i
                break;

        if (split_index != -1):
            #print("{} - {}".format(arr[:split_index], arr[split_index:]))
            A = rec_arr_split(arr[:split_index])
            B = rec_arr_split(arr[split_index:])
            if A >= B:
                return 1 + A
            else:
                return 1 + B            
    return 0

T = int(raw_input())
for i in xrange(0,T):
    try:
        arr_size = int(raw_input())
        arr = [int(s) for s in raw_input().split(" ")]
        print(rec_arr_split(arr))
    except EOFError:
        exit

#didn't pass submission, no idea why

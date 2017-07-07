
from collections import deque


def balance_scales(balanceMap, current_balance):
    B_L = balanceMap[current_balance]['L']
    B_R = balanceMap[current_balance]['R']

    if len(B_L) == 1 and len(B_R) == 1:
        if B_L[0] == 0 and B_R[0] == 0:
            #print("10 {}".format(current_balance))            
            return 10
        elif B_L[0] == B_R[0]:
            return B_L[0]*2 + 10
        elif B_L[0] > B_R[0]:
            #print("L {}".format(current_balance))
            extra = B_L[0] - B_R[0]
            balanceMap[current_balance]['M'] = "{} {}".format('R', extra)
            return B_L[0]*2 + 10
        elif B_R[0] > B_L[0]:
            #print("R {}".format(current_balance))
            extra = B_R[0] - B_L[0]
            balanceMap[current_balance]['M'] = "{} {}".format('L', extra)
            return B_R[0]*2 + 10

    else:
        sum_left = B_L[0]
        sum_right = B_R[0]
        #print("LT{} - {} ".format(current_balance, B_L))
        #print("RT{} - {} ".format(current_balance, B_R))
        if (len(B_L) > 1):
            B_list = B_L[1:]
            for x in B_list:
                sum_left += balance_scales(balanceMap, x)
        if (len(B_R) > 1):
            B_list = B_R[1:]
            for x in B_list:
                sum_right += balance_scales(balanceMap, x)

        if sum_left != sum_right:
            if sum_left > sum_right:
                extra = sum_left - sum_right
                balanceMap[current_balance]['M'] = "{} {}".format('R', extra)
            if sum_right > sum_left:
                extra = sum_right - sum_left
                balanceMap[current_balance]['M'] = "{} {}".format('L', extra)

        #print("S{} - {} {}".format(current_balance, sum_left, sum_right))
    return sum_left+sum_right+10+extra


balancesNum = int(raw_input())
balancesMap = dict()
for i in range(0, balancesNum):
    try:
        L_side = [int(s) for s in raw_input().split(" ")]
        R_side = [int(s) for s in raw_input().split(" ")]
        B = dict()
        B['L'] = L_side
        B['R'] = R_side
        balancesMap[i] = B
    except EORError:
        exit




#balance_scales(balancesMap, 0)
for j in xrange(0, balancesNum):
    balance_scales(balancesMap, j)   


#print(balancesMap)

for key, values in balancesMap.iteritems():
    A_L = 0
    A_R = 0
    if 'M' in values:
        S, W = values['M'].split(" ")
        if S == 'L':
            A_L = W
        else:
            A_R = W
    
    print("{}: {} {}".format(key,A_L,A_R))

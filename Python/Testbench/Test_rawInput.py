a,b,t = [int(s) for s in raw_input().split(" ")]
cI = 0.5*a + 0.5*b
sumV = 1
rem = t
jump = 500

cIJ = int((cI**jump))%(10**9+7)


 
while rem > 0:
    if rem < jump:
        remJ = (cI**rem)%(10**9+7)
        sumV = (sumV*(remJ))%(10**9+7)
        sumV = int(sumV)
        rem = 0
    else:
        sumV = (sumV*cIJ)%(10**9+7)
        sumV = int(sumV)
        rem = rem - jump


print("{} - {}".format(rem, sumV))
#print((cI**t)%(10**9+7))

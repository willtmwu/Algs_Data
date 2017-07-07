T = int(raw_input())
for i in xrange(1,T+1):
    W = raw_input().split(" ")
    S = ""
    for j in xrange(0, len(W)):
        S += W[len(W)-1-j] + " "
    print("Case #{}: {}".format(i, S))

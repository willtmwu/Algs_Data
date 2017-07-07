
def fib_mod(A,B,n):
    if n == 1:
        return A
    elif n == 2:
        return B
    else:
        return fib_mod(A,B,n-1)**2 + fib_mod(A,B,n-2)





A,B,N = [int(s) for s in raw_input().split(" ")]
print(fib_mod(A,B,N))

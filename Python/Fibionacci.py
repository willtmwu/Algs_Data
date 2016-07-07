"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    if position <=2:
        if position == 0:
            return 0
        else:
            return 1
    else:     
        return get_fib(position-1) + get_fib(position-2)

# Test cases
print get_fib(0)
print get_fib(1)
print get_fib(9)
print get_fib(11)


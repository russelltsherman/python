
"""
The Fibonacci Sequence is the series of numbers:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The next number is found by adding up the two numbers before it.

The 2 is found by adding the two numbers before it (1+1)
The 3 is found by adding the two numbers before it (1+2),
And the 5 is (2+3),
and so on!

Example: the next number in the sequence above is 21+34 = 55
"""

"""
fib 
in the fibonacci sequence
given position n calculate the value for that position 
"""


def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

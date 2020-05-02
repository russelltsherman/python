
"""
the product of an integer and all the integers below it; e.g. factorial four ( 4! ) is equal to 24.

"""


def factorial(n):
    if n <= 1:
        return n
    return factorial(n-1) * n

#!/usr/bin/env python3

# : The Russian Peasant's Algorithm

# : Multiply two numbers
# : Requirements: multiply by 2, divide by two, and Add Numbers

# : AKA = Mediation and Duplication Method

# : Inputs -> two numbers
# : Output -> the solution to those two numbers multiplied using the algorithm

import time

CACHE = {}


def caching(a, b):
    key = (a, b)  # define request key

    try:
        z = CACHE[key]  # set acumulator to cache value if it exists
    except KeyError:    # key not present in cache
        x = a
        y = b
        z = 0
        while x > 0:
            if x % 2 == 1:
                z = z + y
            x = x >> 1
            y = y << 1
        CACHE[key] = z  # set cache value for key

    return z


if __name__ == "__main__":
    print(caching(16, 21))  # => 336
    print(caching(21, 16))  # => 336

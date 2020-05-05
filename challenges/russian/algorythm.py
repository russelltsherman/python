#!/usr/bin/env python3

# : The Russian Peasant's Algorithm

# : Multiply two numbers
# : Requirements: multiply by 2, divide by two, and Add Numbers

# : AKA = Mediation and Duplication Method

# : Inputs -> two numbers
# : Output -> the solution to those two numbers multiplied using the algorithm

# 16   21 - ignore even
#  8   42 - ignore even
#  4   84 - ignore even
#  2  168 - ignore even
#  1  336
# ---------------------
# =   336

# 21   16
# 10   32 - ignore even
#  5   64
#  2  128 - ignore even
#  1  256
# ---------------------
# =   336


def russian(a, b):
    x = a
    y = b
    z = 0  # Acumulator
    while x > 0:  # continue until x <= 0
        if x % 2 == 1:  # if x is an odd number
            z = z + y  # add y to acumulator

        x = x // 2  # // does 'floor' division
        y = y * 2

        # alternately can perform binary shift
        # x = x >> 1  # binary shift right
        # y = y << 1  # binary shift left

        # 17 in base 2:         10001 => 17
        # shift all bits right  >> 1
        #                       1000 => 8
        # 17 in base 2:         10001 => 17
        # shift all bits left   << 1
        #                       100010 => 34
    return z


if __name__ == "__main__":
    print(russian(16, 21))  # => 336
    print(russian(21, 16))  # => 336

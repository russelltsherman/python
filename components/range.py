#!/usr/bin/env python3

"""
Syntax
range(start, stop, step)

start	Optional. An integer number specifying at which position to start. 
Default is 0

stop	Required. An integer number specifying at which position to end.

step	Optional. An integer number specifying the incrementation. 
Default is 1

"""

# Create a sequence of numbers from 0 to 5, and print each item in the sequence:
x = range(6)
print("range(6)")
for n in x:
    print(n)

# Create a sequence of numbers from 3 to 19, but increment by 2 instead of 1:
x = range(3, 20, 2)
print("range(3, 20, 2)")
for n in x:
    print(n)

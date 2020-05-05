
"""
You are given an array and asked to find the number of tripets of indices  (i,j,k) such that the elements at those indices are in geometric progression for a given common ratio r and i < j < k.

For example, arr = [1, 4, 16, 64]. 
If r=4, we have [1,4,16] and [4,16,64] at indices (0,1,2) and (1,2,3).

Function Description

countTriplets has the following parameter(s):

arr: an array of integers
r: an integer, the common ratio

It should return the number of triplets forming a geometric progression for a given  as an integer.

"""

from collections import defaultdict


def countTriplets(arr, r):
    count = 0  # Initialize result
    d1 = defaultdict(int)  # track processed elements
    d2 = defaultdict(int)  # track count of triplets
    for i in reversed(arr):  # iterate array descending
        multiple = i*r
        if multiple in d2:  # if multiple exists in count dict
            count += d2[multiple]  # increment count
        if multiple in d1:  # if multiple exists in track dict
            d2[i] += d1[multiple]
        d1[i] += 1  # record in track dict
    return(count)


# first implementation without collections module
# def countTriplets(arr, r):
#     count = 0  # Initialize result
#     d1 = {}  # track processed elements
#     d2 = {}  # track count of triplets
#     for i in reversed(arr):  # iterate array descending
#         multiple = i*r
#         if multiple in d2:  # if multiple exists in count dict
#             count += d2[multiple]  # increment count
#         if multiple in d1:  # if multiple exists in track dict
#             if i in d2:  # record in count dict
#                 d2[i] += d1[multiple]
#             else:
#                 d2[i] = d1[multiple]
#         if i in d1:  # record in track dict
#             d1[i] += 1
#         else:
#             d1[i] = 1
#     return(count)

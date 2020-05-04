
"""
You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. 
You are allowed to swap any two elements. 
You need to find the minimum number of swaps required to sort the array in ascending order.

For example, given the array  we perform the following steps:
i   arr                     swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]

It took 5 swaps to sort the array.

Function Description

sort has the following parameter(s):

arr: an unordered array of integers

"""


def sort(q):
    swapcount = 0
    sorted = {i: False for i in range(len(q))}

    for key, _ in sorted.items():
        pos = key + 1
        while sorted[key] == False:
            if(q[key] == pos):
                sorted[key] = True
            else:
                key2 = q[key]-1
                q[key], q[key2] = q[key2], q[key]
                swapcount += 1
    return(swapcount)

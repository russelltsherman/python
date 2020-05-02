
"""
A left rotation operation on an array shifts each of the array's elements 1 unit to the left. 
For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2] .

"""


def rotate(arr, left_rotations):
    for _ in range(left_rotations):
        arr.append(arr.pop(0))
    return(arr)

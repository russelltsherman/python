
"""
Given a 6x6 2D Array:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass to be a subset of values with indices falling in this pattern:

a b c
  d
e f g

There are 16 hourglasses in a 6x6 array, 
an hourglass sum is the sum of an hourglass' values. 

Calculate the hourglass sum for every hourglass in the array then return the largest hourglass sum.
"""


def hourglass(board):
    largest = 0
    for i in range(4):
        for j in range(4):
            hourglass = [
                board[i][j], board[i][j+1], board[i][j+2],
                board[i+1][j+1],
                board[i+2][j], board[i+2][j+1], board[i+2][j+2]
            ]
            current = sum(hourglass)
            if i == 0 and j == 0:
                largest = current
            else:
                largest = max(largest, current)
    return(largest)

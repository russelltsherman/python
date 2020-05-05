
"""
You are given q queries. Each query is of the form two integers described below:
-  1x: Insert x in your data structure.
-  2y: Delete one occurence of y from your data structure, if present.
-  3z: Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.

The queries are given in the form of a 2-D array queries of size q where queries[i][0] contains the operation, and queries[i][1] contains the data element. For example, you are given array queries = [(1,1),(2,2),(3,2),(1,1),(1,1),(2,1),(3,2)]. 

The results of each operation are:

Operation   Array   Output
(1,1)       [1]
(2,2)       [1]
(3,2)                   0
(1,1)       [1,1]
(1,1)       [1,1,1]
(2,1)       [1,1]
(3,2)                   1

Return an array with the output: [0,1].

Function Description

Complete the freqQuery function in the editor below. 
It must return an array of integers where each element is a 1 if there is at least one element value with the queried number of occurrences in the current array, or 0 if there is not.

freqQuery has the following parameter(s):

queries: a 2-d array of integers
"""


from collections import defaultdict, deque


def frequencyQuery(q):
    arr = defaultdict(int)
    out = deque()
    freq = defaultdict(set)

    for pair in q:
        o, n = pair[0], pair[1]
        if o == 1:
            v = arr[n]
            arr[n] = v + 1

            if n in freq[v]:
                freq[v].remove(n)

            freq[v + 1].add(n)

        elif o == 2:
            v = arr[n]

            if v > 0:
                v = arr[n]
                arr[n] = v - 1

                if n in freq[v]:
                    freq[v].remove(n)

                freq[v - 1].add(n)
        else:
            if freq[n]:
                out.append(1)
            else:
                out.append(0)

    return(list(out))

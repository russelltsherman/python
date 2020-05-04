
"""
given two arrays which are both sorted and distinct
find the number of elements in common

a: 1,5,15,20,30,37
b: 2,5,13,30,32,35,37,42

"""


def common(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        return(sorted(list(a_set & b_set)))
    else:
        return([])

# first iteration
# def common(a, b):
#     com = []
#     for i in a:
#         try:
#             b.index(i)  # raises exception if not found
#             com.append(i)
#         except ValueError:
#             continue
#     return(com)

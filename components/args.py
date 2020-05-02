#!/usr/bin/env python3

"""
    asterisk indicates that a list of arguments is expected
    double asterisk indicates that a dictionary is expected
"""


def F(*args, **kwargs):
    print("%d arguments were provided" % len(args))

    print("%d keyword arguments were provided" % len(kwargs))

    for arg in args:
        print(arg)

    print(kwargs)


F('brown', eyes='blue', hair='brown')

"""
brown
{'eyes': 'blue'}
"""

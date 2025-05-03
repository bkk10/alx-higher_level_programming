#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = tuple_a[0]
    a2 = tuple_b[1]
    b1 = tuple_a[0]
    b2 = tuple_b[1]
    if (len(tuple_a) < 2 and len(tuple_b) < 2):
        return 0
    if (len(tuple_a > 2)):
        return tuple_a[0:2]
    if (len(tuple_b > 2)):
        return tuple_b[0:2]
    return (a1 + b1, a2 + b2)

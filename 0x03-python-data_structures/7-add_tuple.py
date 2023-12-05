#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    y = (0, 0)
    if len1 < 2:
        tuple_a += y
    elif len2 < 2:
        tuple_b += y

    tu = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return tu

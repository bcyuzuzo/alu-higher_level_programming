#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    a1 = tuple_a + (0, 0)
    b1 = tuple_b + (0, 0)

    res = a1[0] + b1[0], a1[1] + b1[1]

    return res

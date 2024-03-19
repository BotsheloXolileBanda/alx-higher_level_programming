#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    newone = [0, 0]
    for i in range(2):
        newone[i] = tuple_a[i] + tuple_b[i]
    return tuple(newone)

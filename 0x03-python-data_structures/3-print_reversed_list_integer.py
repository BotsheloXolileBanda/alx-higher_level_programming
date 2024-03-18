#!/usr/bin/python3

def print_reversed_list_integer(mylist=[]):
    revlis = mylist.reverse()
    leng = len(mylist)
    for i in range(leng):
        print("{:d}".format(mylist[i]))

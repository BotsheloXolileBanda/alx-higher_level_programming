#!/usr/bin/python3

def print_list_integer(mylist=[]):
    leng = len(mylist)
    for i in range(leng):
        print("{:d}".format(mylist[i]))

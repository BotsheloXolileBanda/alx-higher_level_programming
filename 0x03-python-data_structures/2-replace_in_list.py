#!/usr/bin/python3

def replace_in_list(mylist, idx, element):
    if (idx < 0):
        return mylist
    elif (idx >= len(mylist)):
        return mylist
    else:
        mylist[idx] = element
        return mylist

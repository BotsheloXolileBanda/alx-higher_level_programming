#!/usr/bin/python3

def no_c(my_string):
    newstr = ""
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        else:
            newstr += my_string[i]
    return str(newstr)

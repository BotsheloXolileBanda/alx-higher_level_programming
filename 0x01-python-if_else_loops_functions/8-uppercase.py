#!/usr/bin/python3

def uppercase(str):
	for x in str:
	    if ord(x) >= 97 and ord(x) <= 123:
	        print("{}".format(chr(ord(x) - 32)), end="")
	    else:
	        print("{}".format(chr(ord(x))), end="")

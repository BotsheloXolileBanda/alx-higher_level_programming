#!/usr/bin/python

def print_last_digit(number):
	if number < 0:
	    lastdig = (number * -1) % 10
	    print(lastdig, end="")
	    return lastdig
	else:
	    lastd = number % 10
	    print(lastd, end="")
	    return lastd

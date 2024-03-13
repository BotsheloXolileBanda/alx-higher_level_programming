#!/usr/bin/python3

for y in range(0, 100):
	if y == 99:
	    print("{:02d}".format(y))
	else:
	    print("{:02d}".format(y), end=", ")

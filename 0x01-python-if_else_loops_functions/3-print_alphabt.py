#!/usr/bin/python3

for y in range(97, 123):
	if y == 101 or y == 113:
	    continue
	else:
	    print("{}".format(chr(y)), end="")

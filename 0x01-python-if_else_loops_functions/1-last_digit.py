#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdig = ((number * -1) % 10)
    if lastdig == 0:
        print(f"Last digit of {number} is 0 and is 0")
    else:
        print(f"Last digit of {number} is -{lastdig} and is less than 6 and not 0")
else:
    lastdi = (number % 10)
    if lastdi > 5:
        print(f"Last digit of {number} is {lastdi} and is greater than 5")
    elif lastdi == 0:
        print(f"Last digit of {number} is 0 and is 0")
    else:
        print(f"Last digit of {number} is {lastdi} and is less than 6 and not 0")

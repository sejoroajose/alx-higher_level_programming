#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10

msg = "and is "

if last > 5:
    msg += "greater than 5"
elif last == 0:
    msg += "0"
else:
    msg += f"less than 6 and not 0"

print(f"Last digit of {number} is {last} {msg}")

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
temp = number % 10
if temp > 5:
    print(f"Last digit of {number} is {temp} and is greater than 5")
elif temp == 0:
    print(f"Last digit of {number} is {temp} and is and is 0")
elif temp < 6 and not 0:
    print(f"Last digit of {number} is {temp} and is less than 6 and not 0")

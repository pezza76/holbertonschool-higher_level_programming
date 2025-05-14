#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is {str(number)[-1]} is ", end = " ")
if str(number)[-1] > 5:
    print("and is greater than 5")
elif str(number)[-1] == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")

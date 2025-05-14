#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            result = chr(ord(i) - 32)
        else:
            result = chr(ord(i))
        print("{}".format(result), end="")
    print()

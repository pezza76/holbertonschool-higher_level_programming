#!/usr/bin/python3

def islower(c):
    for i in c:
        if ord(i) >= ord('a') and ord(c) <= ord('z'):
            print("{}".format(chr(ord(i) - 32)), end="")
    else:
        print(i, end="")

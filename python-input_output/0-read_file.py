#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """function that reads a text file"""
    with open(filename) as f:
        print(f.read(), end="")

#!/usr/bin/python3
"""Append text to a file"""


def append_write(filename="", text=""):
    """function that adds a string to the end of a text file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)

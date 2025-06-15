#!/usr/bin/python3
"""Prints a sorted list"""


class MyList(list):
    """Prints a list"""
    def print_sorted(self):
        print(sorted(self))

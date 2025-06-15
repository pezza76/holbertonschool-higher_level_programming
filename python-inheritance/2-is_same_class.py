#!/usr/bin/python3
"""Check class of object"""


def is_same_class(obj, a_class):
    """Checks class of object"""
    if type(obj) == type(a_class):
        return type(obj) is a_class
    else:
        return False

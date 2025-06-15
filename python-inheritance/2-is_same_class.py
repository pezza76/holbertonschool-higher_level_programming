#!/usr/bin/python3
"""Check class of object"""


def is_same_class(obj, a_class):
    """Checks class of object"""
    if type(obj) == type(a_class):
        return True
    else:
        return False

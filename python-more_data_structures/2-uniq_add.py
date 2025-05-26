#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = set(my_list)
    total = 0
    for i in result:
        total = total + i
    return total

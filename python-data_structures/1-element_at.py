#!/usr/bin/python3

def element_at(my_list, idx):
    for i in range(len(my_list)):
        if idx < 0:
            return None
        elif idx >= len(my_list):
            return None
        elif my_list[i] == my_list[idx]:
            print("element at index {} is {}".format(idx, my_list[idx]))

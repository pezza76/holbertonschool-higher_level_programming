#!/usr/bin/python3

def read_file(filename=""):
    """function that reads a text file"""
    
    with open(filename) as f:
        print(f.read())

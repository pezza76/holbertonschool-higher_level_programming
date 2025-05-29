#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """Square class with a private size attribute."""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
    
    def my_print(self):
        for _ in range(self.__size):
            if self.__size == 0:
                print()
                return
            for i in range(self.__size):
                    print("#", end="")
            print()

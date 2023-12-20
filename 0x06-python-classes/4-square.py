#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute,
size verification, and a public instance method for calculating the area.
"""


class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes the square with an optional size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size ** 2

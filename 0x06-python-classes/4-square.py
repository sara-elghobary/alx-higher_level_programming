#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute,
properties for getting and setting the size, and a public instance method for
calculating the area.
"""


class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes the square with an optional size.

        Parameters:
        - size (int): The size of the square. Default is 0.

        Raises:
        - TypeError: If the provided size is not an integer.
        - ValueError: If the provided size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size.

        Parameters:
        - value (int): The size of the square.

        Raises:
        - TypeError: If the provided size is not an integer.
        - ValueError: If the provided size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

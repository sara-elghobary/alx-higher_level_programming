#!/usr/bin/python3
"""
This module defines a class Square with private instance attributes for size
and position, properties for getting and setting them, and public instance
methods for calculating the area and printing the square.
"""


class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with optional size and position.

        Parameters:
        - size (int): The size of the square. Default is 0.
        - position (tuple): The position of the square. Default is (0, 0).

        Raises:
        - TypeError: If the provided size is not an integer.
                     If the provided position is not a tuple
                     of two positive integers.
        - ValueError: If the provided size is less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter method for retrieving the position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for setting the position.

        Parameters:
        - value (tuple): The position of the square.

        Raises:
        - TypeError: If the provided position is not a
        tuple of two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(val, int) and val >= 0 for val in value):
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character # and considering the position.

        If size is equal to 0, prints an empty line.
        Position should be used by using space - Don’t
        fill lines by spaces when position[1] > 0.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

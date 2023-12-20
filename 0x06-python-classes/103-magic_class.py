#!/usr/bin/python3
import math

class MagicClass:
    """
    This class represents a MagicClass that works with circles.
    It includes methods for calculating the area and circumference of a circle.
    """

    def __init__(self, radius=0):
        """
        Initializes the MagicClass instance with a given radius.

        Parameters:
        - radius (int or float): The radius of the circle. Default is 0.

        Raises:
        - TypeError: If the provided radius is not an integer or float.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
        - float: The area of the circle.
        """
        return self.__radius**2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
        - float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius

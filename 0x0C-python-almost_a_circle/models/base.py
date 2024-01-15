#!/usr/bin/python3


class Base:
    """Base class with private class attribute __nb_objects"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor for Base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

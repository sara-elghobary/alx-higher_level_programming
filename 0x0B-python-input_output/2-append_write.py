#!/usr/bin/python3
"""
Contains the append_write function
"""


def append_write(filename="", text=""):
    """""appends a string at the end of a text file
      and returns the number of characters added:

"""
    with open(filename, "a", encoding="utf-8") as f:
        s = f.write(text)
        return s

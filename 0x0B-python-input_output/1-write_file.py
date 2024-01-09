#!/usr/bin/python3
"""
Contains the write_file function
"""


def write_file(filename="", text=""):
    """""write in a text file and return the number of characters written"""
    with open(filename, "w", encoding="utf-8") as f:
        s = f.write("text")
        return s

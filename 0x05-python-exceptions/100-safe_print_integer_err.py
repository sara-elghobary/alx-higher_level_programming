#!/usr/bin/python3
import sys

from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as e:
        stderr.write("Exception: {}\n".format(e))
        return (False)

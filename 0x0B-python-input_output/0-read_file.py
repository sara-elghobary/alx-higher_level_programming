#!/usr/bin/python3
def read_file(filename=""):
    """
    Read the contents of a file and print them to the console.

    Parameters:
    - filename (str): The name of the file to be read. If not
    provided, an empty string is used.

    Returns:
    None
    """
    with open(filename, encoding="UTF-8") as myfile:
        print(myfile.read())

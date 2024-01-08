#!/usr/bin/python3

def text_indentation(text):
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty result string
    result = ""

    # Define the characters that trigger a new line
    new_line_characters = ['.', '?', ':']

    # Iterate through each character in the input text
    for char in text:
        # Add the character to the result string
        result += char

        # If the character is one of the trigger characters, add two new lines
        if char in new_line_characters:
            result += '\n\n'

    # Split the result string into lines and print each line
    for line in result.split('\n'):
        print(line.strip())


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")

#!/usr/bin/python3

"""Function that writes a string to a text file"""


def write_file(filename="", text=""):
    """writing the string into the open file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return (f.write(text))

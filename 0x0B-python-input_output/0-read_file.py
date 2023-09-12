#!/usr/bin/python3

"""function that reads a text file"""


def read_file(filename=""):
    """openning a file in utf-8 and reading its content"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")

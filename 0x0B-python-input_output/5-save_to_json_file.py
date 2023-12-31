#!/usr/bin/python3

"""
function that writes an Object to a text file using JSON rep.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    opening a file to save the object to a text file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(json.dumps(my_obj)))

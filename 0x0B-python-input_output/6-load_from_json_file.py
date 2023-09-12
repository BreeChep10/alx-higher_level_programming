#!/usr/bin/python3

"""
function that creates an object from a json file
"""
import json


def load_from_json_file(filename):
    """
    opening the json file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return (json.load(f))

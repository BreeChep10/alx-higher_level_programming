#!/usr/bin/python3

"""
script that adds all arguements toa Python list.
"""
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    exists = load_from_json_file("add_item.json")
except FileNotFoundError:
    exists = []

"""
getting command line arguements ie the script name.
"""
new = sys.argv[1:]
updates = exists + new

"""
save the updated list as a json representation
"""
save_to_json_file(updates, "add_item.json")

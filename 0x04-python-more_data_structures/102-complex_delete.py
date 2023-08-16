#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    delete_keys = []
    for i, j in a_dictionary.items():
        if j == value:
            delete_keys.append(i)
    for delete in delete_keys:
        del a_dictionary[delete]

    return a_dictionary

#!/usr/bin/python3

def no_c(my_string):
    store = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            store += i
    return store

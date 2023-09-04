#!/usr/bin/python3

"""
a module to print nouns

"""

def say_my_name(first_name, last_name=""):

    """
    A function to print input nouns

    @first_name: the first name
    @second_name: the second name

    Retutn: nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name != "":
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))

#!/usr/bin/python3

def uppercase(str):

    uppercase_str = ""

    for i in str:
        if 'a' <= i <= 'z':
            uppercase_char = chr(ord(i) - 32)
            uppercase_str += "{}".format(uppercase_char)
        else:
            uppercase_str += "{}".format(i)
    
    print(uppercase_str)

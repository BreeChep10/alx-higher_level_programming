#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if 'a' <= i <= 'z':
            uppercase_char = chr(ord(i) - 32)
            print(uppercase_char, end="")
        else:
            print(i, end="")
    print()

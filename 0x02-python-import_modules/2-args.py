#!/usr/bin/python3

from sys import argv


if __name__ == "__main__":
    no_args = len(argv) - 1
    args = argv[1:]

    print("{} arguement{}{}".format(
        no_args,
        's' if no_args != 1 else '',
        ':' if no_args > 0 else '.'))

    for i in range(len(args)):
        pos = i + 1
        arg = args[i]
        print("{}: {}".format(pos, arg))
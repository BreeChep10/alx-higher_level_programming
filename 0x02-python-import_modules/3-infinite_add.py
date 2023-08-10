#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    args = argv[1:]

    sum_no = 0
    for i in range(len(args)):
        arg = args[i]
        sum_no += int(arg)
    print(sum_no)

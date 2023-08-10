#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    args = argv[1:]

    sum_no = 0
    for i in range(len(args)):
        arg = args[i]
        sum_no += int(arg)
    print(sum_no)

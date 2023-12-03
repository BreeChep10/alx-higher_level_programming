#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    nums = len(sys.argv) - 1
    args = sys.argv[1:]

    for i in range(len(args)):
        if nums == 0:
            print(f"{nums} arguments")
        else:
            print(f"{nums}, argument:\n", i + 1, ":", args[i])

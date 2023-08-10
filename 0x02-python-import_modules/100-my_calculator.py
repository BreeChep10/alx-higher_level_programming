#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    no_args = len(sys.argv) - 1
    args = sys.argv[1:]

    if no_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        operator = sys.argv[2]

        if operator not in ("+", "-", "*", "/"):
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:

            if operator == "+":
                addition = add(int(sys.argv[1]), int(sys.argv[3]))
                print(sys.argv[1], operator, sys.argv[3], "=", addition)

            elif operator == "-":
                subtraction = sub(int(sys.argv[1]), int(sys.argv[3]))
                print(sys.argv[1], operator, sys.argv[3], "=", subtraction)

            elif operator == "*":
                prod = mul(int(sys.argv[1]), int(sys.argv[3]))
                print(sys.argv[1], operator, sys.argv[3], "=", prod)

            elif operator == "/":
                division = div(int(sys.argv[1]), int(sys.argv[3]))
                print(sys.argv[1], operator, sys.argv[3], "=", division)

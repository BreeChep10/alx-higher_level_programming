#!/usr/bin/python3


from calculator_1 import add, sub, mul, div

a = 10
b = 5

addition = add(a, b)
subtraction = sub(a, b)
product = mul(a, b)
division = div(a, b)

print("{} + {} = {}".format(a, b, addition))
print("{} + {} = {}".format(a, b, subtraction))
print("{} + {} = {}".format(a, b, product))
print("{} + {} = {}".format(a, b, division))
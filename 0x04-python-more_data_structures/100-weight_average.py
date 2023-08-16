#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    sum_prods = 0
    sum_weights = 0

    for score, weight in my_list:
        sum_prods += score * weight
        sum_weights += weight

    if sum_weights == 0:
        return 0

    return sum_prods / sum_weights

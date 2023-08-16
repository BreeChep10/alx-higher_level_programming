#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum_nums = 0
    seen = set()

    for i in range(len(my_list)):
        if my_list[i] not in seen:
            sum_nums += my_list[i]
            seen.add(my_list[i])
    return sum_nums

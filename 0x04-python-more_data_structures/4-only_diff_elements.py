#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    temp = set()
    for i in set_1:
        if i not in set_2:
            temp.add(i)
    for j in set_2:
        if j not in set_1:
            temp.add(j)
    return temp

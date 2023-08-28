#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            if (type(my_list_1[i]) not in (int, float) or
                    type(my_list_2[i]) not in (int, float)):
                result.append(0)
                print("wrong type")
            elif my_list_2[i] == 0:
                result.append(0)
                print("division by 0")
            else:
                result.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        except IndexError:
            result.append(0)
            print("out of range")
        except Exception:
            result.append(0)

    return result

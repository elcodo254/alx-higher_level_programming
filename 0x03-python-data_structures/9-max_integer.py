#!/usr/bin/python3
def max_integer(my_list=[]):
    maximum = -9999

    if my_list == []:
        return None
    else:
        for dgt in my_list:
            if dgt > maximum:
                maximum = dgt

    return maximum

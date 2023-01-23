#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        dval = a / b
    except (TypeError, ZeroDivisionError):
        dval = None
    finally:
        print("Inside result: {}".format(dval))
    return dval

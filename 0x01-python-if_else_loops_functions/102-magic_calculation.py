#!/usr/bin/python3
def magi_calculation(a, b, c):
    if a < b:
        return c
    elif b < c:
        return a + b
    else:
        return (a * b) - c

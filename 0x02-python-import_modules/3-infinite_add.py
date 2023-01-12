#!/usr/bin/python3
def add(amnt, arg):
    total = 0
    if amnt > 1:
        for i in range(1, amnt):
            total += int(arg[i])

    return total
if __name__ == "__main__":
    from sys import argv
    print("{:d}".format(add(len(argv), argv)))

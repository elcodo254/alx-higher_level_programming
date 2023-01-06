#!/usr/bin/python3
for letter in range(122, 96, -1):
    if letter % 2 == 0:
        print(f"{letter:c}", end="")
    else:
        print(f"{letter - 32:c}", end="")

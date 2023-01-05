#!/usr/bin/python3
def print_last_digit(number):
    lastdgt = number % 10
  #  if number < 0:
   #     lastdgt = (-number) % 10
    #else:
     #   lastdgt = number % 10

    print(f"{lastdgt:d}", end="")
    return lastdgt

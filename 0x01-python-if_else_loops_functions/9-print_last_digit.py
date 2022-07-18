#!/usr/bin/python3
def print_last_digit(number):
    number = int(repr(number)[-1])
    if number >= 0:
        print("{}".format(number % 10))
        return number % 10
    else:
        print("{}".format(number % - 10))
        return number % -10

#!/usr/bin/python3
# this makes the code unexcutable when imported
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    c = add(a, b)
    print("{} + {} = {}".format(a, b, c))

#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # first part checks elements not in set 2 from
    # set one and vice versa for 2nd part
    # | combines the two sets to create a
    # new set containgi the unique elements from both sets
    present_one = (set_1 - set_2) | (set_2 - set_1)
    return present_one

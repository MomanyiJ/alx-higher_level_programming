#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiply_dict = {}
    # k = key, v = value
    for k, v in a_dictionary.items():
        multiply_dict[k] = v * 2
    return multiply_dict


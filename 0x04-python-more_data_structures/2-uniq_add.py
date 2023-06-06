#!/usr/bin/python3
def uniq_add(my_list=[]):
    total_sum = 0
    # we use the set function cause it takes unique integers
    for num in set(my_list):
        total_sum += num

    return total_sum

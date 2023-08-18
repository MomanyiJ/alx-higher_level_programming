#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):  # check if index is given is valid
        return str
    new_str = ""
    for i in range(len(str)):
        if i != n:
            new_str += str[i]
        
    return new_str

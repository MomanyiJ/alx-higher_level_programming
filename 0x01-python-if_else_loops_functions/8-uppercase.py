#!/usr/bin/python3
def uppercase(str):
    let = ''
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            let += chr(ord(char) - 32) # converts lower to uppercase
        else:
            let += char
    print("{}".format(let))

#!/usr/bin/python3
'''contains class Mylist'''


class MyList(list):
    '''subclass of list'''

    def __init__(self):
        '''Initialize object'''
        super().__init__()

    def print_sorted(self):
        '''prints sorted list'''
        print(sorted(self))

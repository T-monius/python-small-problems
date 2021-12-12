'''A module for finding duplicates in lists'''

def find_dup(lst):
    '''Find a duplicate value in a list and return it'''
    seen = {}

    for val in lst:
        if seen.get(val, False):
            return val

        seen[val] = True

'''A module for determining the middle character(s) of a string'''

def is_odd(num):
    '''Determine if a number is odd'''
    return num % 2 != 0


def middle_two_chars(target, center):
    '''Retrieve the middle two characters of a string of even length'''
    return target[center - 1:center + 1]


def center_of(target):
    '''Return the one or two characters representing the middle of a
       string input'''
    _len = len(target)
    center = int(_len / 2)
    mid = target[center] if is_odd(_len) else middle_two_chars(target, center)

    return mid

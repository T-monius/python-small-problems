'''A module for working with uppercase characters of strings'''

def is_uppercase(target):
    '''Return a boolean indicating whether all alpha characters of a
       target string are uppercase'''
    for char in target:
        if char.isalpha():
            if char.upper() != char:
                return False

    return True

'''A module for transforming sting letter cases'''

def swapcase(normal_case, swapped=''):
    '''Return a new string with the case of the alpha characters
       swapped'''
    idx = len(swapped)
    if idx == len(normal_case):
        return swapped

    char = normal_case[idx]
    if char.isalpha():
        if char.islower():
            char = char.upper()
        else:
            char = char.lower()

    swapped += char

    return swapcase(normal_case, swapped)

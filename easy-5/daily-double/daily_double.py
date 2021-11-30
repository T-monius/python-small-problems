'''A module for working with strings that have duplicate characters'''

def crunch(input_str):
    '''Remove consecutive duplicate characters from a string returning
        a new string'''
    collapsed_str = ''
    for char in input_str:
        if not collapsed_str or char != collapsed_str[-1]:
            collapsed_str += char

    return collapsed_str

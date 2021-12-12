'''A module for searching a list for values'''

def does_include(lst, search_val):
    '''Return boolean whether a value is present in an array'''
    for val in lst:
        if val == search_val:
            return True

    return False

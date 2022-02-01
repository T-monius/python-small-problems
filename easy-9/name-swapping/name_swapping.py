'''A module for changing the order of a name and surname'''

def swap_name(name):
    '''Swap the first name and last name of an input string and
       separate by a comma and a space instead of a space'''
    names = name.split()
    names[1], names[0] = names[0], names[1]
    swapped = ', '.join(names)

    return swapped

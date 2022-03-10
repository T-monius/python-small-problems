'''A module for creating strings which print to diamonds formed by
   starts/asteriscs'''

def calculate_stars(stars, line, midpoint):
    '''Calculate the number of stars according to the line and midpoint
       given'''
    if (line <= midpoint) and (line != 0):
        stars += 2
    elif line > midpoint:
        stars -= 2

    return stars


def add_spaces_and_stars(target_str, spaces, stars):
    '''Add the number of spaces and stars to a target string'''
    target_str += (' ' * spaces)
    target_str += ('*' * stars)
    target_str += '\n'

    return target_str


def diamond(num):
    '''Return a string that prints to a diamond of the height of the
       input integer formed by stars/asteriscs'''
    midpoint = int(num / 2)
    dmd = ''
    stars = 1

    for line in range(0, num):
        stars = calculate_stars(stars, line, midpoint)
        spaces = int((num - stars) / 2)
        dmd = add_spaces_and_stars(dmd, spaces, stars)

    return dmd

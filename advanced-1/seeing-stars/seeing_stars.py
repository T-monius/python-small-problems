'''A module for outputing star grids by certain dimensions'''

SPACE = ' '
STAR = '*'

def calculate_spaces(line, middle, last_idx):
    '''Determine how many leading spaces and spaces between stars
       based on line, middle line, and last index'''
    is_before_middle = line < middle

    if is_before_middle:
        distance_from_middle = middle - line
        leading_space = line
    else:
        distance_from_middle = line - middle
        leading_space = last_idx - line
    spaces = distance_from_middle - 1

    return leading_space, spaces


def middle_line(stars):
    '''Return a line of n stars based on the input'''
    middle_gridline = f"{STAR * stars}\n"

    return middle_gridline


def starry_line(line, middle, last_idx):
    '''Return a starry line based on the current line, middle line,
       and last index'''
    leading_space, spaces = calculate_spaces(line, middle, last_idx)

    gridline = f'{SPACE * leading_space}{STAR}' \
               f'{SPACE * spaces}{STAR}' \
               f'{SPACE * spaces}{STAR}\n'

    return gridline


def star_power_grid(rows):
    '''Return a sring of line separated rows of asterisks spaced
       per line number to form an 8 point star'''
    middle = int(rows / 2)
    last_idx = rows - 1
    grid = ''

    for line in range(0, rows):
        gridline = middle_line(rows) if line == middle else starry_line(line, middle, last_idx)

        grid += gridline

    return grid

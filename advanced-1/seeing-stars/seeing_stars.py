'''A module for outputing star grids by certain dimensions'''

def star_power_grid(rows):
    '''Return a sring of line separated rows of asterisks spaced
       per row number to form an 8 point star'''
    middle = int(rows / 2)
    last_idx = rows - 1
    grid = ''
    for row in range(0, rows):
        if row == middle:
            grid += f"{'*' * rows}\n"
            continue
        is_before_middle = row < middle
        if is_before_middle:
            distance_from_middle = middle - row
            leading_space = row
        else:
            distance_from_middle = row - middle
            leading_space = last_idx - row
        spaces = distance_from_middle - 1
        gridline = f'{" " * leading_space}*{" " * spaces}*{" " * spaces}*\n'
        grid += gridline

    return grid

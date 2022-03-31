'''A module for determining the type of triangle from its sides'''

def is_valid_triangle(sides):
    '''Determine whether sorted sides of a triangle are valid'''

    # All sides must be greater than zero
    if not sides[0] > 0 or not sides[1] > 0 or not sides[2] > 0:
        return False
    # Two shortest sides must sum to a greater length than longest
    if not (sides[0] + sides[1]) > sides[2]:
        return False

    return True


def triangle(side_zero, side_one, side_two):
    '''Return a triangle's classification based on its sides else
       invalid'''
    sides = [side_zero, side_one, side_two]
    sides.sort()

    if not is_valid_triangle(sides):
        return 'invalid'

    # All sides are equal
    if sides[0] == sides[1] and sides[1] == sides[2]:
        return 'equilateral'
    # Two sides are equal
    if ((sides[0] != sides[1] and sides[1] == sides[2]) or
        (sides[0] == sides[1] and sides[1] != sides[2])):
        return 'isosceles'

    # No equal sides
    return 'scalene'

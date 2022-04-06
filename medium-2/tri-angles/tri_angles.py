'''A module to identify triangle types by their angles'''

def triangle(angle_zero, angle_one, angle_two):
    '''Return a string representing whether a triangle composed of
       three angles as input is right, acute, obtuse, or invalid'''
    angles = [angle_zero, angle_one, angle_two]
    if 0 in angles or sum(angles) != 180:
        return 'invalid'

    if angle_zero < 90 and angle_one < 90 and angle_two < 90:
        return 'acute'
    if angle_zero == 90 or angle_one == 90 or angle_two == 90:
        return 'right'
    if angle_zero > 90 or angle_one > 90 or angle_two > 90:
        return 'obtuse'

    return 'invalid'

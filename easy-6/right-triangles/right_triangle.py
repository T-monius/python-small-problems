'''A module for working with visual output to stdOut'''

def triangle(num):
    '''Print a right triangle as wide and tall as input number'''
    for stars in range(1, num):
        spaces = num - stars
        print(f'{" " * spaces}{"*" * stars}')


triangle(5)
print('\n')
triangle(9)
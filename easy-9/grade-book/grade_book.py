'''A module for determining letter grades from number scores'''

def average_of_three(num, num_one, num_two):
    '''Return the average of three numbers'''
    total = sum([num, num_one, num_two])
    int_average = int(total / 3)

    return int_average


def letter_grade(score):
    '''Return a letter grade from a score'''
    if score > 100 or score < 0:
        return 'Indeterminable'
    if score > 90:
        return 'A'
    if score > 80:
        return 'B'
    if score > 70:
        return 'C'
    if score > 60:
        return 'D'

    return 'F'


def get_grade(grade, grade_one, grade_two):
    '''Retun a letter grade based on the average of three numeric
       scores'''
    avg = average_of_three(grade, grade_one, grade_two)
    letter = letter_grade(avg)

    return letter

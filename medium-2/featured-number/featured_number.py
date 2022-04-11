'''A module for working with featured numbers which are odd multiples
   of seven that have unique digits'''

LIMIT = 9_999_999_999

def next_multiple_of_seven(num):
    '''Find the next multiple of seven greater than an input number'''
    for successor in range(num + 1, num + 8):
        if successor % 7 == 0:
            return successor

    return None


def is_all_unique_digits(num):
    '''Return whether all of the digits of a number are unique'''
    seen = set()
    for digit in str(num):
        if digit in seen:
            return False
        seen.add(digit)

    return True


def next_featured_num(num):
    '''Return the next number greater than the input number that is a
       featured number'''
    if num >= LIMIT:
        return None

    next_seven = next_multiple_of_seven(num)

    for multiple_of_seven in range(next_seven, LIMIT, 7):
        if multiple_of_seven % 2 != 0 and \
            is_all_unique_digits(multiple_of_seven):

            return multiple_of_seven

    return None

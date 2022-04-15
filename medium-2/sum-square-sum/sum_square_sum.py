'''A module to work with summing the positive integers then squaring
   or squaring positive integers then summing'''

def pos_ints_upto_num_inclusive(limit):
    '''Return a list of the positive integers up to a limit inclusive'''
    return list(range(1, limit + 1))


def calculate_square_sum(integers):
    '''Calculate the sum of an integer list, then square it.'''
    return sum(integers) ** 2


def calculate_sum_of_squares(integers):
    '''Square the elments of an input list of integers, then sum the
       the squared numbers.'''
    return sum([num ** 2 for num in integers])


def sum_square_difference(limit):
    '''Return the difference between the 'square sum' and 'sum of
       squares' from an integer list limited by the input integer'''
    integers = pos_ints_upto_num_inclusive(limit)
    square_sum = calculate_square_sum(integers)
    sum_of_squares = calculate_sum_of_squares(integers)

    return square_sum - sum_of_squares

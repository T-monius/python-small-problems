'''A module for derivig a list containing a sequence of number'''

def sequence(count,initial_int):
    '''Reuturn a list of numbers by the length of a given count
       starting from the initial number. Members of the sequence
       are multiples of the initial number'''
    seq = []

    for multiplier in range(1, count + 1):
        product = initial_int * multiplier
        seq.append(product)

    return seq

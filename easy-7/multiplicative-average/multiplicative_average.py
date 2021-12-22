'''A module for finding averages from lists'''
from functools import reduce

def multiply(num, num1):
    '''Multiply two numbers and return the product'''
    product = num * num1
    return product


def show_multiplicative_average(ints):
    '''Find the average of the product of elements in a list'''
    total_of_products = reduce(multiply, ints)

    return round(total_of_products / len(ints), 3)

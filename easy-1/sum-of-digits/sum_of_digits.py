'''A Module for working with the digits of an integer'''
from functools import reduce

def sum(num, num1):
	return num + num1

def sum_of_digits(integer):
	str_digits = list(str(integer))
	digits = list(map(int, str_digits))
	total = reduce(sum, digits)

	return total

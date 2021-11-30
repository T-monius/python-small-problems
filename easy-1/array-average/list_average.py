'''A module for testing averages'''
from functools import reduce

def sum(num, num1):
	return num + num1

def average(integers):
	'''Calculate the integer average of a list of input integers'''
	total = reduce(sum, integers)

	# divide the total of all integers by the number of integers
	return int(total / len(integers))
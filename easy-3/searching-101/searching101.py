"""A module to test of a number is among a list of numbers"""
from random import randint

def six_random_numbers():
	numbers = []

	for num in range(0, 6):
		numbers.append(randint(0, 1000))

	return numbers

def is_number_present():
	num = randint(0, 1000)
	numbers = six_random_numbers()
	is_present = num in numbers

	return [ num, is_present, numbers ]

if __name__ == '__main__':
	num, is_present, numbers = is_number_present()

	if is_present:
		print(f'The number {num} appears in {numbers}')
	else:
		print(f'The number {num} does not appear in {numbers}')

'''A module for int to str conversion'''

def number_to_string(num):
	'''Convert an int input to a str'''
	if num == 0:
		return '0'

	digits = []

	while num > 0:
		num, rem = divmod(num, 10)
		digits.append(rem)

	string_digits = [ str(num) for num in digits]
	string_digits.reverse()
	return ''.join(string_digits)


def signed_int_to_str(num):
	'''Convert an int to a signed number'''
	if num == 0:
		return number_to_string(num)

	if num < 0:
		absolute_value = abs(num)
		return '-' + number_to_string(absolute_value)
	else:
		return '+' + number_to_string(num)

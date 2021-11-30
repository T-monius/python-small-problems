def digit_list(num):
	'''Retrieve the digits of a positive number'''
	quotient = num
	digits = []

	while quotient > 0:
		quotient, rem = divmod(quotient, 10)
		digits.append(rem)

	digits.reverse()
	return digits

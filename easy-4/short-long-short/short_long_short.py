'''A module for working with string inputs'''

def short_long_short(string_zero, string_one):
	shorter = (string_zero if len(string_zero) < len(string_one) else string_one)
	longer = (string_zero if len(string_zero) > len(string_one) else string_one)

	return f'{shorter}{longer}{shorter}'
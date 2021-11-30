'''A module for assessing ASCII values of a str'''

def ascii_string_value(input_string):
	chars = list(input_string)
	ascii_values = [ord(char) for char in chars]
	return sum(ascii_values)
# from ..odd.odd import is_odd
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'odd'))
from odd import is_odd

def binary_string(num):
	bin_str = ''

	for num in range(0, num):
		if is_odd(num):
			bin_str += '0'
		else:
			bin_str += '1'

	return bin_str
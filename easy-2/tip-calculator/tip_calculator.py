"""A module for calculating a tip"""

def tip_calculator():
	'''Prompt user for bill and tip rate. Output tip and total'''
	bill_prompt = 'How much was the bill?\n'
	tip_prompt = 'What percentage would you like to tip?\n'

	bill = float(input(bill_prompt))
	tip_rate = float(input(tip_prompt)) / 100

	tip = bill * tip_rate
	total = bill + tip

	print(f'Your bill total is: {total}')
	print(f'The tip is: {tip}')


if __name__ == '__main__':
	tip_calculator()
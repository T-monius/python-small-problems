'''A module for calculating salary bonuses for employees'''

def calculate_bonus(salary, is_bonus):
	if not salary or salary < 0:
		return

	bonus = 0

	if is_bonus:
		bonus = int(salary / 2)

	return bonus
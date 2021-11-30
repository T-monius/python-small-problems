"""Module for calculating a person's retirement age"""

def retirement_age():
	age_prompt = 'What is your age? '
	age_to_retire_prompt = 'At what age would you like to retire? '

	current_age = int(input(age_prompt))
	desired_retirement_age = int(input(age_to_retire_prompt))

	years_to_retirement = desired_retirement_age - current_age
	retirement_year = 2021 + years_to_retirement

	print(f"It's 2021. You will retire in {retirement_year}")


if __name__ == '__main__':
	retirement_age()

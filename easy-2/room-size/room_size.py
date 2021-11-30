"""A module for considering the dimensions of a room."""

def calculate_room_area():
	"""Prompt user for length and width of a room and calculate area"""
	length_prompt = "Please enter the length of the room in meters:\n"
	width_prompt = "Please enter the width of the room in meters:\n"
	quit_msg = 'Enter "q" or "quit" at any time to exit.'

	print(quit_msg)
	length_str = input(length_prompt)

	if length_str == 'q' or length_str == 'quit':
		print('quitting...')
		return

	print(quit_msg)
	width_str = input(width_prompt)

	if width_str == 'q' or width_str == 'quit':
		print('quitting...')
		return

	length = int(length_str)
	width = int(width_str)
	area = length * width

	print(f'The area of the room is {area} square meters ({area * 3.281} square eet).')

if __name__ == '__main__':
	calculate_room_area()

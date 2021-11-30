# repeat_yourself.py

def repeat(input_str, num):
	count = 0
	while count < num:
		print(input_str)
		count += 1

repeat('Hello', 3)
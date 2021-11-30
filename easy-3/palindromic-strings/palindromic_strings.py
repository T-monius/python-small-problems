def is_palindrome(some_string):
	anchor = 0
	end_idx = len(some_string) - 1

	while anchor < end_idx:
		char = some_string[anchor]
		char1 = some_string[end_idx]

		if char != char1:
			return False

		anchor += 1
		end_idx -= 1

	return True


def is_not_alpha(char):
	ordinal_value = ord(char)
	return ordinal_value < 97 or ordinal_value > 122


def is_not_numeric(char):
	ordinal_value = ord(char)
	return ordinal_value < 48 or ordinal_value > 57	


def is_real_palindrome(some_string):
	some_string_lowercase = some_string.lower()
	anchor = 0
	end_idx = len(some_string_lowercase) - 1

	while anchor < end_idx:
		char = some_string_lowercase[anchor]
		char1 = some_string_lowercase[end_idx]

		if is_not_alpha(char) and is_not_numeric(char):
			anchor += 1
			continue

		if is_not_alpha(char1) and is_not_numeric(char1):
			end_idx -= 1
			continue

		if char != char1:
			return False

		anchor += 1
		end_idx -= 1

	return True


def is_palindromic_number(num):
	numeric_string = str(num)
	return is_real_palindrome(numeric_string)

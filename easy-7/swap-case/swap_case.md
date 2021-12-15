# Swap Case

## Problem

Write a function that takes a string as an argument and returns a new string in which every uppercase letter is replaced by its lowercase version, and every lowercase letter by its uppercase version. All other characters should be unchanged.

You may not use String#swapcase; write your own version of this function.

### Understanding

Input
- String
	- Arbitrary length
	- Arbitrary characters
Output
- String
	- Alpha characgters opposite of input string

## Examples / Test Cases

```python
swapcase('CamelCase') == 'cAMELcASE'
swapcase('Tonight on XYZ-TV') == 'tONIGHT ON xyz-tv'

# 'CamelCase'
#  ^
new_str = ''
idx = len(new_str)  # 0
char = input_str[0] # C

'''
Return if new_str is the same length as input_str
If the current char isalpha
	- If it's lower
		- Re-assign upper version to char
	- If it's upper
		- Re-assign lower version the char
Push char to new_str
Call with the input_str, new_str
'''
```

# The Middle Char

## Problem

Write a function that takes a non-empty string argument, and returns the middle character or characters of the argument. If the argument has an odd length, you should return exactly one character. If the argument has an even length, you should return exactly two characters.

### Understanding

Input
- String
	- Non-empty
Output
- String
	- One or two character length
		- Represents the middle portion / slice
		- Even length string
			- Two character returned
		- Odd length string
			- One character returned

## Examples / Test Cases

```python
center_of('I love ruby') == 'e'
center_of('Launch School') == ' '
center_of('Launch') == 'un'
center_of('Launchschool') == 'hs'
center_of('x') == 'x'

'''
Middle point for an odd length
- Divide by 2

'''
odd_target = 'I love ruby'
#              ^
target_len = 11
# 11/2 = 5.5
# floor = 5
midpoint = 5
middle_char = 'e'
'''
Middle point for an even length

'''
even_target = 'Launch'
#                ^ ^
# 6 / 2 = 3
midpoint = 3
middle_chars = even_target[midpoint - 1:midpoint + 1]
```

## Data Structures

- N / A

## Algorithm
Functional Abstractions
- N / A

1. Determine length of string
2. Calculate `midpoint` variable
3. Declare `mid` variable
4. Branch for 'odd' or 'even' length
5.   Odd
 			 Set `mid` character at `midpoint`
6.   Even
			 Set `mid` a slice between one before or after `midpoint`
7. Return `mid`

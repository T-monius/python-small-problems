# Name Swapping

## Problem

Write a function that takes a first name, a space, and a last name passed as a single String argument and returns a string that contains that last name, a comma, a space, and the first name.

### Understanding

Input
- String
	- Name
	- Space separated
		- First name
		- Last name
Output
- String
	- Swapped input names
	- Comma-space separated

## Examples / Test Cases

```python
swap_name('Joe Roberts') == 'Roberts, Joe'

name = 'Joe Roberts'
names = ['Joe', 'Roberts']
swapped_names = ['Roberts', 'Joe']
```

## Data Structures

- List

## Algorithm

1. Split the input string
2. Swap names
3. Join with comma and space

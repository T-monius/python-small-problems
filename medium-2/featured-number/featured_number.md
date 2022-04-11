# Next Featured Number Higher than a Given Value

## Problem

A featured number (something unique to this exercise) is an odd number that is a multiple of 7, and whose digits occur exactly once each. So, for example, 49 is a featured number, but 98 is not (it is not odd), 97 is not (it is not a multiple of 7), and 133 is not (the digit 3 appears twice).

Write a function that takes a single integer as an argument, and returns the next featured number that is greater than the argument. Return an error message if there is no next featured number.

### Understanding

Featured number is an Integer that is:
- Multiple of 7
- Odd
- Each of its digits are unique

Input
- Single integer
Output
- single Integer
	- Next greater featured number
	- In other words,
		- Next multiples of 7 THAT...
		- also is odd AND...
		- has unique digits

## Examples / Test Cases

```python
featured(12) == 21
featured(20) == 21
featured(21) == 35
featured(997) == 1029
featured(1029) == 1043
featured(999_999) == 1_023_547
featured(999_999_987) == 1_023_456_987

featured(9_999_999_999) # -> There is no possible number that fulfills those requirements

num = 12

current_num = 21
# current_num divisible by 7? => YES
# curren_num odd? => YES
# current_num digits unique? YES
```

## Data Structures

- String
- Set

## Algorithm

1. Find the next multiple of seven (utility method)
	1. Guard clauses
		  - Negative?
		  - Not a number?
	1. Iterate from one greater than the num to eight greater
	2.   If the number is a multiple of seven return it
	3. Return `None`
2. Iterate a range from next multiple to limit with a step of seven
3.   - Interrogate number for oddity
4.   - Interrogate number for unique digits
5.   - Return number if both conditions pass
6. Return `None`

- `is_all_unique_digits`
	1. Coerce number to a string
	2. Instantiate an empty set `seen`
	3. Iterate characters of string
	4.   If the character has been seen, return `False`
  5.   Add the character to the set
  6. Return `True`

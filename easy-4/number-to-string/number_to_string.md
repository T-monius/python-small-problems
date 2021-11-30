# Convert a Number to a String!

## Problem

In the previous two exercises, you developed methods that convert simple numeric strings to signed Integers. In this exercise and the next, you're going to reverse those methods.

Write a method that takes a positive integer or zero, and converts it to a string representation.

You may not use any of the standard conversion methods available in Python. Your method should do this the old-fashioned way and construct the string by analyzing and manipulating the number.

### Understanding

Can convert with chr and/or a dictionary

## Examples / Test Cases

```python
integer_to_string(4321) == '4321'
integer_to_string(0) == '0'
integer_to_string(5000) == '5000'

'''
digits = []
num, rem = divmod(4321, 10)
num = 432
rem = 1
digits = [1]
num, rem = divmod(num, rem)
num = 43
rem = 2
digits = [1, 2]
...
digits = [1, 2, 3, 4]
'''
```

## Data Structures

- Array

## Algorithm
### Functional Abstractions
- Transformation

### Hard Algorithm

- Insattiate an empty list for converted digits
- Iterate over number while it's greater than 0
	- re-assign number to the result of 10 division
	- Assign remainder to a variable
	- Append remainder to array of digits
- Use a _list comprehension_ to 'map' digits to strings
- Reverse mapped digits and join

## Problem 2
### Convert a Signed Number to a String!

In the previous exercise, you developed a method that converts non-negative numbers to strings. In this exercise, you're going to extend that method by adding the ability to represent negative numbers as well.

Write a method that takes an integer, and converts it to a string representation.

You may not use any of the standard conversion methods available in Python. You may, however, use `integer_to_string` from the previous exercise.

### Understanding

Signed numbers differ in being negative, positive, or zero

## Examples / Test Cases

```python
signed_integer_to_string(4321) == '+4321'
signed_integer_to_string(-123) == '-123'
signed_integer_to_string(0) == '0'
```

## Data Structures

- N/A

## Algorithm

- Early return for zero
- Test a number for negativity
- Conditionally prepend `-` or `+`

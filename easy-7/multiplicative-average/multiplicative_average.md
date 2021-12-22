# Multiplicative Average

## Problem

Write a function that takes an List of integers as input, multiplies all the numbers together, divides the result by the number of entries in the List, and then prints the result rounded to 3 decimal places. Assume the list is non-empty.

### Understanding

Input
- List
	- Integer elements
Output
- A float (quotient of multiplying and dividing int elements)
	- Multiply all of the nubers
	- Divivide result by list length

## Examples / Test Cases

```python
show_multiplicative_average([3, 5])                # => The result is 7.500
show_multiplicative_average([6])                   # => The result is 6.000
show_multiplicative_average([2, 5, 7, 11, 13, 17]) # => The result is 28361.667

'''
[3, 5]


3 * 5 => 15 / 2 #=> 7.5
'''
```

## Data Structures

- N / A

## Algorithm
Functional Abstractions
- Reduce

1. Define a reduction helper to multiply to elements
2. Reduce the list
3. Divide by length and return

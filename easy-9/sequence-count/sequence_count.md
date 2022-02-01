# Sequence Count

## Problem

Create a function that takes two integers as arguments. The first argument is a count, and the second is the first number of a sequence that your function will create. The function should return an List that contains the same number of elements as the count argument, while the values of each element will be multiples of the starting number.

You may assume that the count argument will always have a value of 0 or greater, while the starting number can be any integer value. If the count is 0, an empty list should be returned.

### Understanding

Input
- 2 arguments
	- Integers
		1. Count
		2. First number of a sequence
Output
- List
	- Length, count
	- Values = multiples of the starting number

Count always 0 or greater
Starting number, any integer (even negative)

## Examples / Test Cases

```python
sequence(5, 1) == [1, 2, 3, 4, 5]
sequence(4, -7) == [-7, -14, -21, -28]
sequence(3, 0) == [0, 0, 0]
sequence(0, 1000000) == []

count = 5
starting_int = 1
seq = [1, 2]
multiplier = 2

# multiplier x current_int
# 2 				 x 1
# 2
```

## Data Structures

- List

## Algorithm
Functional abstractions
- Iteration

1. Declare a list for return
2. Delacre a multiplier starting from 1
3. Iterate over a range from 1 up the count + 1
4. 	 Multiply the number at iteration by the starting number
5.   Push it to the return list
6. Return the return list

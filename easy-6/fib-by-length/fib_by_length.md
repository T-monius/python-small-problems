# Fibonacci Number Location By Length

## Probmlem

The Fibonacci series is a series of numbers (1, 1, 2, 3, 5, 8, 13, 21, ...) such that the first 2 numbers are 1 by definition, and each subsequent number is the sum of the two previous numbers. This series appears throughout the natural world.

Computationally, the Fibonacci series is a very simple series, but the results grow at an incredibly rapid rate. For example, the 100th Fibonacci number is 354,224,848,179,261,915,075 -- that's enormous, especially considering that it takes 6 iterations before it generates the first 2 digit number.

Write a function that calculates and returns the index of the first Fibonacci number that has the number of digits specified as an argument. (The first Fibonacci number has index 1.)

### Understanding

Fibomacci
- Number series
	- First 2 numbers are 1
	- Each subsequent number = sum of previous two nums
- Computationally
	- Results grow rapidly
	- 100th number is huge
	- Takes 6 iterations to reach 2 digit num

Function
- Input
	- Number
		- Digit length of number in Fibonacci series
- Output
	- Number
	- Index of first number with input length
		- 1 indexed

`Argument >= 2`

## Examples / Test Cases

```python
find_fibonacci_index_by_length(2) == 7          # 1 1 2 3 5 8 13
find_fibonacci_index_by_length(3) == 12         # 1 1 2 3 5 8 13 21 34 55 89 144
find_fibonacci_index_by_length(10) == 45
find_fibonacci_index_by_length(100) == 476
find_fibonacci_index_by_length(1000) == 4782
find_fibonacci_index_by_length(10000) == 47847

desired_len = 2

'1 1 2 3 5 8 13'
#          ^
idx1 = 5
idx2 = 8
current_idx = 7
val = 13

# Calculate val
# Is len(val) == desired_len ?
# 	Return
# Call recursively
```

# Sum Square - Square Sum

## Problem

Write a function that computes the difference between the square of the first `n` positive integers and the sum of the squares of the first `n` positive numbers.

### Understanding

Input
- Integer
	- Represents the inclusive limit of a range from `1` to `n`
Output
- Integer
	- Represents a calculation
		- Sum members of range then square
		- Square members then sum.
		- Subtract second calculation from first

## Examples / Test Cases

```python
sum_square_difference(3) == 22
   # -> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)
sum_square_difference(10) == 2640
sum_square_difference(1) == 0
sum_square_difference(100) == 25164150
```

## Data Structures

- Range
- List

## Algorithm

1. Use a list comprhension or range to derive list of elements
2. `square_sum` = Reduce/sum the elements and square
3. `sum_of_squares` = Map/list comprehension the elements to square
4.   Reduce
5. Return `sum_of_square - square_sum`

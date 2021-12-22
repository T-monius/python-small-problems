# Multiply Lists

## Problem

Write a function that takes two List arguments in which each List contains a list of numbers, and returns a new List that contains the product of each pair of numbers from the arguments that have the same index. You may assume that the arguments contain the same number of elements.

### Understanding

Input
- Two lists
	- Integer elements
	- Same lengths
Output
- List
	- Integer elements
	- products of matching indexes from input array

## Examples / Test Cases

```python
multiply_list([3, 5, 7], [9, 10, 11]) == [27, 50, 77]
```

## Data Structures

- N / a

## Algorithm
Functional Abstractions
- Iteration / map

1. Declare a new `products` variable
2. Declare `idx` variable setting to `0`
3. Iterate over first array
	- Access index of secondary array
	- Push product of element at iteration with other element
4. Return products

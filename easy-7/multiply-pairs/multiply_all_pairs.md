# Multiply All Pairs

## Problem

Write a function that takes two List arguments in which each List contains a list of numbers, and returns a new List that contains the product of every pair of numbers that can be formed between the elements of the two Lists. The results should be sorted by increasing value.

You may assume that neither argument is an empty List.

### Understanding

Input
- Two lists
	- Number elements
Output
- List
	- Number elements
		- Ordered
		- Products
			- Each element of first array multiplied by each element of second array

## Examples / Test Cases

```python
multiply_all_pairs([2, 4], [4, 3, 1, 2]) == [2, 4, 4, 6, 8, 8, 12, 16]

'''
primary = [2, 4] | secondary = [4, 3, 1, 2]
					    ^
					    		   	    						   ^
products = [8, 6, 2, 4, 16, 12, 4, 8]
ordered = [2, 4, 4, 6, 8, 8, 12, 16]

current_el = 4
secondary_el = 2
product = 8
'''
```

## Data Structures

- List

## Algorithm
Functional Abstractions
- Iteration
- Ordering

1. Declare a list `products` to push to
2. Iterate over `primary` list
	- Iterate over `secondary` list
		- Multiply value at primary by secondary
		- Push to `products`
3. Order and return `products`

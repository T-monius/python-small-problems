# Grocery List

## Problem

Write a function which takes a grocery list (List) of fruits with quantities and converts it into a List of the correct number of each fruit.

### Understanding

Input
- List
	- List elements
		- Sub lists
			- String
			- Number: quantity
Output
- List
	- No nesting
	- Count / quantity elements of each sublist

## Examples / Test Cases

```python
buy_fruit([["apples", 3], ["orange", 1], ["bananas", 2]]) ==
  ["apples", "apples", "apples", "orange", "bananas","bananas"]

[["apples", 3], ["orange", 1], ["bananas", 2]]
# 	   							^
current_list = ["orange", 1]

products = ["apples", "apples", "apples", "orange"]
```

## Data Structures

- List

## Algorithm
Functional Abstractions
- Reduction

1. Declare return `products` List
2. Iterate over input List
3.   For range from 0 up to quantity
4. 	   Append products to `products` list
5. Return products list

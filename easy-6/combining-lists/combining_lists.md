# Combining Lists

## Problem

Write a function that takes two Lists as arguments, and returns an Array that contains all of the values from the argument Lists. There should be no duplication of values in the returned Array, even if there are duplicates in the original Lists.

### Understanding

Input
- 2 args
	- Lists
Output
- A single list
	- Combination of input list
	- No duplicates

If all number inputs or of similar data types, sorting then combining would be ideal.
- Efficient
However, not explicitly stated that the list would contain similar data types.
- Using a dictionary may suit the problem

### Examples / Test Cases

```python
merge([1, 3, 5], [3, 6, 9]) == [1, 3, 5, 6, 9]
# 		    ^
#                    ^
seen = { 1:True, 3:True, 6:True, 5:True, 9:True}
new_list = [1, 3, 6, 5, 9]
```

## Data Structures

- Dictionary

## Algorithm
Functional Abstractions
- Iteration

1. Declare a new return list
2. Declare and empty dictionary `seen`
3. Declare 2 index values to 0
4. Iterate while both indexes is are less then their list lengths
	- Access values at iteration
	- For both value, evaluate if it's been seen
		- if not append to the new list
	- Increment both indexes
5. If either index is less than the length of corresponding list continue iterating
6. Return new list
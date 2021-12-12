# Halvsies

## Problem

Write a function that takes a List as an argument, and returns two Lists (as a pair of nested Lists) that contain the first half and second half of the original List, respectively. If the original List contains an odd number of elements, the middle element should be placed in the first half List.

### Understanding

Input
- Single argument
	- List
Output
- Single argument
	- List
		- Nested lists
		- First and second half of input
			- Longer being first if odd input length
			- Middle value in first list

Can handle with iteration
Can handle with slicing

## Examples / Test Cases

```python
halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]]
halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]]
halvsies([5]) == [[5], []]
halvsies([]) == [[], []]

lst = [1, 2, 3, 4]
#            m

lst = [1, 5, 2, 4, 3]
#            m

middle_idx = int(len(lst) / 2) #=> 2
```

## Data Structures

- Arrays

## Algorithm

1. Find the middle of the array
2. Return a nesting of two slices up to the middle index and after

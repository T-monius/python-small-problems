# Merge Sorted Lists

## Problem

Write a function that takes two sorted Lists as arguments, and returns a new List that contains all elements from both arguments in sorted order.

You may not provide any solution that requires you to sort the result list. You must build the result list one element at a time in the proper order.

Your solution should not mutate the input lists.

### Understanding

Input
- 2 arguments
	- Lists
		- Integer elements
		- Sorted
Output
- List
	- Sorted
	- Elements of input lists combined
  - Must build one element at a time in order

Cannot sort

## Examples / Test Cases

```python
merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9]
merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3]
merge([], [1, 4, 5]) == [1, 4, 5]
merge([1, 4, 5], []) == [1, 4, 5]

arr = [1, 5, 9]
#         ^

arr1 = [2, 6, 8]
#       ^

new_len = len(arr) + len(arr1)   #=> 6
merged = [1, ]
idx = 1
idx1 = 0


'''

Iterate new_len times
  el = 1
  el1 = 2

  if el < el1
      Append el to merged
      Increment its index
  else
      Append el1 to merged
      Increment its index

Return merged
'''
```

## Data Structures

- Lists

## Algorithm
Functional Abstraction
- Iteration

1. Set `new_len` to length of two lists
2. Set `merged` to an empty list
3. Instantiate variables for list indexes to zero
4. Iterate over a range from zero up to `new_len`
5.     Set `val` to value at `ints[idx]`
6.     Set `val1` to value at `ints[idx1]`
7.     if el < el1
8.         Append el to merged
9.         Increment its index
0.     else
1.         Append el1 to merged
2.         Increment its index
3. Return merged

# Reversed Lists

## Problem

Write a function that takes a List as an argument, and reverses its elements in place; that is, mutate the List passed into this method. The return value should be the same List object.

You may not use built in methods.

### Understanding

Swap in place to reverse
Ruby allows for parallel assignment which allows for in place swapping.
Whether or not Python allows for this, the same can be accomplished with intermiate variables

## Examples / Test Cases

```python
lst = [1,2,3,4]
#			 ^
# 					 ^
# 		[4,2,3,1]
# 		   ^
#			 		 ^
# 		[4,3,2,1]

result = reverse!(lst)
result == [4, 3, 2, 1] # true
lst == [4, 3, 2, 1] # true
lst.object_id == result.object_id # true

lst = %w(a b e d c)
reverse!(lst) == ["c", "d", "e", "b", "a"] # true
lst == ["c", "d", "e", "b", "a"] # true

lst = ['abc']
reverse!(lst) == ["abc"] # true
lst == ["abc"] # true

lst = []
reverse!(lst) == [] # true
lst == [] # true
```

## Data Structures

- N/A

## Algorithm
- Functional Abstractions
	- Iteration
1. Declare two pointers to first and last index
2. Iterate while the first pointer is less than the second
	- At each iteration
	- Access elements at iteration
	- Set elements at iteration to separate variables
	- Assign each variable to the opposite index (first to last, last to first)
	- Increment first idx
	- Decrement second idx
3. Return List

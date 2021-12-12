# Find The Duplicate

## Problem

Given an unordered list and the information that exactly one value in the list occurs twice (every other value occurs exactly once), how would you determine which value occurs twice? Write a method that will find and return the duplicate value that is known to be in the list.

### Understanding

Input
- Unordered list
	- One duplicate
Output
- Duplicate value

## Examples / Test Cases

```python
lst = [7, 2, 22, 5, 5, 6, 3]
#                   ^

seen = {7: True, 2:True, 22:True, 5:True}

find_dup(lst)
#=> 5
```

## Data Structures

- Dictionary

## Algorithm

- Iteration

1. Declare an empty dictionary to track `seen` elements
2. Iterate over list
	- For each element if it's already been `seen`, return it
	- Else, save in the `seen` dictionary

# Rotation

## Problem

Write a function that rotates a List by moving the first element to the end of the list. The original list should not ve modified.

### Understanding

Input
- List
	- Arbitrary length
	- Arbitrary element type
Output
- New list
- Elements modified by one position
- First element moved to the end

## Examples / Test Cases

```python
rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7]
rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a']
rotate_list(['a']) == ['a']

x = [1, 2, 3, 4]
rotate_list(x) == [2, 3, 4, 1]   # => True
x == [1, 2, 3, 4]                 # => True

lst = [7, 3, 5, 2, 9, 1]
#      ^
rotated = []

# el = lst[0]
# rotated = lst[1:]
# rotated + el
```

## Problem 2

Write a function that can rotate the last `n` digits of a number.

Note that rotating just 1 digit results in the original number being returned.
You may use the `rotate_list` function from the previous exercise if you want. (Recommended!)
You may assume that n is always a positive integer.

### Understanding

Equivalent to slicing `n` elements from the end of the list, rotating, then re-appending.

## Examples / Test Cases

```python
rotate_rightmost_digits(735291, 1) == 735291
rotate_rightmost_digits(735291, 2) == 735219
rotate_rightmost_digits(735291, 3) == 735912
rotate_rightmost_digits(735291, 4) == 732915
rotate_rightmost_digits(735291, 5) == 752913
rotate_rightmost_digits(735291, 6) == 352917
```

## Data Structures

- List

## Algorithm

1. Convert num to a string then list
1. Set a new prefix list to a slice from `0` up to the length of the list minus the `n`
2. Set suffix to a slice from negative `n` to the end of the list
3. Rotate the suffix
4. Append rotated suffix to the prefix
5. Join list
6. Convert joined list to a number and return

# All Substrings

## Problem

Write a function that returns a list of all substrings of a string. The returned list should be ordered by where in the string the substring begins. This means that all substrings that start at position 0 should come first, then all substrings that start at position 1, and so on. Since multiple substrings will occur at each position, the substrings at a given position should be returned in order from shortest to longest.

You may (and should) use the leading_substrings function you wrote in the previous exercise:

### Understanding

Input
- String

Output
- List
	- All substrings of input string
		- Ordered
			- Position dictates order
			- All substrings starting from index `0`, then increasing
			- Order at a position dictated by length

## Examples / Test Cases

```python
# 					 len
target = 'abcde'
#   			^
# 				 ^

all_substrings = ['a', 'ab', 'abc', 'abcd', 'abcde', 'b', 'bc', 'bcd', 'bcde']
```

## Data Structures

- List

## Algorithm

- Set length of input string to a variable, `target_len`
- Set `idx` for first pointer to `0`
- Declare an empty return list, `all_substrings`
- Return `all_substrings` if `idx` `target_len` is less than `1`
- While `idx` is less than `target_len`
	- Set `upto_idx` for second pointer to `idx + 1`
	- While `upto_idx` is less than or equal to `target_len`
		- Slice the input string, `target`, from `idx` to `upto_idx`
		- Append slice to the return list
		- Increment `upto_idx`
	- Increment `idx`
- Return `all_substrings`

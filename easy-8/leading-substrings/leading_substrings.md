# Leading Substrings

## Problem

Write a function that returns a list of all substrings of a string that start at the beginning of the original string. The return value should be arranged in order from shortest to longest substring.

### Understanding

Input
- String
Output
- List
	- All substrings starting from start

Can solve with a continually incrementing index and a return list

## Examples / Test Cases

```python
leading_substrings('abc') == ['a', 'ab', 'abc']
leading_substrings('a') == ['a']
leading_substrings('xyzzy') == ['x', 'xy', 'xyz', 'xyzz', 'xyzzy']

'''
input = 'abc'
 				   ^
lst = ['a', 'ab', 'abc']
'''
```

## Data Structures

- String
- List

## Algorithm
Functional abstractions
- Reduction? OR Transformation?

Recursive Function
- `idx` and `strs` parameters
	- `idx` set to `1`
	- `strs` is an empty list by default
- Base case
	- `idx` is greater than the length of the the input string
	- OR string is empty
	- Return `strs`
- Push a slice up to the `idx` to the return array
- Return a recursive call to the function

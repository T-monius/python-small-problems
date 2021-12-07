# Delete Vowels

## Problem

Write a function that takes a List of strings, and returns a List of the same string values, except with the vowels (a, e, i, o, u) removed.

### Understanding

Input
- Array
	- String elements
Output
- Array
	- String elements
		- No vowels (a, e, i, o, u)


## Examples / Test Cases

```python
remove_vowels(['abcdefghijklmnopqrstuvwxyz']) == ['bcdfghjklmnpqrstvwxyz']
remove_vowels(['green', 'YELLOW', 'black', 'white']) == ['grn', 'YLLW', 'blck', 'wht']
remove_vowels(['ABC', 'AEIOU', 'XYZ']) == ['BC', '', 'XYZ']

lst = ['green', 'YELLOW', 'black', 'white']
#				^

new_list = ['grn']
current_word = 'green' #-> 'grn'
#								 ^
```

## Data Structures

- List

## Algorithm
### Functional Abstractions
- Transformation
- Interrogation

## Steps

1. List comprehension (Map)
	- Invoke `replace` on every word at iteration w/ regex for vowels

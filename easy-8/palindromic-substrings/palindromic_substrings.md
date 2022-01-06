# Palindromic Substrings

## Problem

Write a function that returns a list of all substrings of a string that are palindromic. That is, each substring must consist of the same sequence of characters forwards as it does backwards. The return value should be arranged in the same sequence as the substrings appear in the string. Duplicate palindromes should be included multiple times.

You may (and should) use the substrings function you wrote in the previous exercise.

For the purposes of this exercise, you should consider all characters and pay attention to case; that is, "AbcbA" is a palindrome, but neither "Abcba" nor "Abc-bA" are. In addition, assume that single characters are not palindromes.

### Understanding

Input
- String
Output
- List
	- Substrings that are palindromes

- Palindromes
	- All characters
	- Case matters
	- Single characters are not

## Examples / Test Cases

```python
palindromes('abcd') == []
palindromes('madam') == ['madam', 'ada']
palindromes('hello-madam-did-madam-goodbye') == [
  'll', '-madam-', '-madam-did-madam-', 'madam', 'madam-did-madam', 'ada',
  'adam-did-mada', 'dam-did-mad', 'am-did-ma', 'm-did-m', '-did-', 'did',
  '-madam-', 'madam', 'ada', 'oo'
]
palindromes('knitting cassettes') == [
  'nittin', 'itti', 'tt', 'ss', 'settes', 'ette', 'tt'
]

ex = 'm-did-m'
#     ^
#           ^

ex1 = 'settes'
```

## Data Stuctures

- List

## Algorithm
Functional Abstractions
- Selection / Filtering

- Get all subbstrings
- Filter list of all substrings for palindromes

- `is_palindromic`
	- Case matters
	- Compare character over character
		- No checks for special characters
		- No checks for whitespace

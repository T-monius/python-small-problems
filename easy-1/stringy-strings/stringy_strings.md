# Stringy Strings

## Problem

Write a method that takes one argument, a positive integer, and returns a string of alternating 1s and 0s, always starting with 1. The length of the string should match the given integer.

### Understanding

Input
- Positive integer
Output
- String
	- Alternating 1s and 0s
	- Starting from 1
	- Length of string matches input integer
Cam multiply a string with asterisk in Python3
If the string always starts from 1, then odd indices are 0, and others 1.

## Examples / Test Cases

```ruby
puts stringy(6) == '101010'
puts stringy(9) == '101010101'
puts stringy(4) == '1010'
puts stringy(7) == '1010101'
```

## Data Structures

- N/A

## Algorithm

1. Declare return string
2. Iterate from 0 to input integer
	1. Conditionally push `0` if num is odd
	2. Else, push `1`
3. Return binary string

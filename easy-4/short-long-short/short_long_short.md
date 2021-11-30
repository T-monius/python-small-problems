# Short Long Short

## Problem

Write a method that takes two strings as arguments, determines the longest of the two strings, and then returns the result of concatenating the shorter string, the longer string, and the shorter string once again. You may assume that the strings are of different lengths.

### Understanding

Input
- Two Strings
Output
- Single string
	- Concatenation of short, long, short

1. Determine longest of two strings
2. Concatenate short, long, short

## Examples / Test Cases

```python
short_long_short('abc', 'defgh') == "abcdefghabc"
short_long_short('abcde', 'fgh') == "fghabcdefgh"
short_long_short('', 'xyz') == "xyz"
```

## Data Structures

- String

## Algorithm
### Functional Abstractions

- Interrogation

### Steps

1. Assign shorter and longer variables
2. Return variables concatenated

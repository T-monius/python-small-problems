# ASCII String Value

## Problem

Write a method that determines and returns the ASCII string value of a string that is passed in as an argument. The ASCII string value is the sum of the ASCII values of every character in the string. (You may use `ord` to determine the ASCII value of a character.)

### Understanding

Input
- String
Outpu
- Integer
	- Sum of ASCII values of input string characters

## Examples / Test Cases

```python
ascii_value('Four score') == 984
ascii_value('Launch School') == 1251
ascii_value('a') == 97
ascii_value('') == 0
```

## Data Structures

- N/A

## Algorithm
### Functional Abstractions

- Map / reduce

## Hard Algorithm

- Convert the string to a list
- Use a list comprehension to map characters to ASCII values
- Sum with `sum` or `reduce` or a `for` loop

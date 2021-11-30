# Alphabetical Numbers

## Problem

Write a function that takes a List of Integers between 0 and 19, and returns a List of those Integers sorted based on the English words for each number:

zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen

### Understanding

Function
Input
- List
	- Integer
		- Between `0` and `19`
Output
- List
	- Integers
	- Sorted
		- English names

Dictionary can store integers as keys, English word as values
1. Built in and Library functions
`List.sort()`
- Take a sorting function?
	- 2nd argument `key` is a single argument function
Does Python's `sorted` method take a sorting function?
2. Transform, sort, transform

## Examples / Test Cases

```python
alphabetic_number_sort(list(range(0, 20))) == [
  8, 18, 11, 15, 5, 4, 14, 9, 19, 1, 7, 17,
  6, 16, 10, 13, 3, 12, 2, 0
]
```

## Data Structures

- Dict

## Algorithm
### Functional Abstractions
Transformation
Sorting
Transformation

### Hard Algorithm
1. Create two dictionaries
	- Int -> English word
	- English word -> Int
2. Map (List Comprehension) nums to English Words
3. Sort English words
4. Map sorted English words to nums
5. Return

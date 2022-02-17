# Grade book

## Problem

Write a fucntion that determines the mean (average) of the three scores passed to it, and returns the letter value associated with that grade.

### Understanding

Input
- 3 Arguments
	- Numbers
Output
- String
	- Letter Grade
		- Result of averaging inputs

## Examples / Test Cases

```python
get_grade(95, 90, 93) == "A"
get_grade(50, 50, 95) == "D"
```

## Data Structures

- N / A

## Algorithm

Function to find average
- Sum numbers
- Divide by three

Function to return grade
- Early return for a number less than Zero or Greater than 100
- Return `'A'` if greater than or equal to `90`
- ...

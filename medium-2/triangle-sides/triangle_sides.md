# Triangle Sides

## Problem

A triangle is classified as follows:

- __equilateral__ All 3 sides are of equal length
- __isosceles__ 2 sides are of equal length, while the 3rd is different
- __scalene__ All 3 sides are of different length

To be a _valid triangle_, the sum of the lengths of the two shortest sides must be greater than the length of the longest side, and all sides must have lengths greater than 0: if either of these conditions is not satisfied, the triangle is invalid.

Write a function that takes the lengths of the 3 sides of a triangle as arguments, and returns a string `'equilateral'`, `'isosceles'`, `'scalene'`, or `'invalid'` depending on whether the triangle is equilateral, isosceles, scalene, or invalid.

### Understanding

Valid Triangle
- Input
	- 3 numbers
	- Represent sides of a triangle
- Output
	- Symbol
		- 4 options
		- Type or invalid

Invalid
- Sum of two shortest lengths less than longest
- Any length zero or less

## Example / Test Cases

```python
triangle(3, 3, 3) == 'equilateral'
triangle(3, 3, 1.5) == 'isosceles'
triangle(3, 4, 5) == 'scalene'
triangle(0, 3, 3) == 'invalid'
triangle(3, 1, 1) == 'invalid'

side = 3
side1 = 3
side2 = 3

sides = [side, side1, side2] #=> [3, 3, 3]
# All > 0 => True
# Sum of first 2 greater than third => True
# Valid
# Equilateral? => three sides equal ? => True
# return 'equilateral'

side = 3
side1 = 3
side2 = 1.5

sides = [side2, side, side1] #=> [1.5, 3, 3]
# All > 0 => True
# Sum of first 2 greater than third => True
# Valid
# Equilateral? => three sides equal ? => False
# Isoceles => two sides equal ? => True
# return 'isoceles'

side = 3
side1 = 4
side2 = 5

sides = [side, side1, side2] #=> [3, 4, 5]
# All > 0 => True
# Sum of first 2 greater than third => True
# Valid
# Equilateral? => three sides equal ? => False
# Isoceles => two sides equal ? => False
# Scalene => no conditions/default
# return 'scalene'
```

## Data Structures

- List

## Algorithm

1. Put sides in a list `sides` and sort
2. Create a `is_valid_triangle` function
3.   Return `False` if any side is not greater than zero
4.   Return `False` if first two sides aren't greater than third
5.   Return `True`
6. Return `'invalid'` if the triangle isn't valid
7. Conditions to return `'equilateral` or `'isocoles'`
8. Return `'scalene'`

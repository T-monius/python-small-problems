# Seeing Stars

## Problem

Write a function that displays an 8-pointed star in an `n` x `n` grid, where `n` is an odd integer that is supplied as an argument to the function. The smalles such star you need to handle is a 7x7 grid.

### Understanding

Input
- Integer
	- Odd
	- 7 or greater
Output
- Asterisks and whitespece
- As 8 asterisks on outer verical columns, rows
- As many asterisks on center row as input integer
- 3 Asterisks on every other row
	- Space separated at incementing values from center

## Examples / Test Cases

```python
star(7)

'''
*  *  *
 * * *
  ***
*******
  ***
 * * *
*  *  *
'''

row = 0
middle = 3 																		 #=> int(7 / 2)
las_idx = 6 																	 #=> len(input_num) - 1
is_before_middle = True
  distance_from_middle = middle - row 				 #=> 3
	leading_spaces = row												 #=> 0
space_between_stars = distance_from_middle - 1 #=> 2
# ...
row = 4
middle = 3 																		 #=> int(7 / 2)
is_before_middle = False
  distance_from_middle = row - middle 				 #=> 1
	leading_spaces = last_idx - row              #=> 2
space_between_stars = distance_from_middle - 1 #=> 0

star(9)

'''
*   *   *
 *  *  *
  * * *
   ***
*********
   ***
  * * *
 *  *  *
*   *   *
'''

row = 0
middle = 4 																		 #=> int(9 / 2)
is_before_middle = True
  distance_from_middle = middle - row 				 #=> 4
  leading_spaces = row												 #=> 0
space_between_stars = distance_from_middle - 1 #=> 3
# ...
row = 5
middle = 4 																		 #=> int(9 / 2)
last_idx = 8
is_before_middle = False
  distance_from_middle = row - middle 				 #=> 1
  leading_spaces = last_idx - row   					 #=> 3
space_between_stars = distance_from_middle - 1 #=> 0
```

## Data Structures

String

## Algorithm

1. Calculate `middle`
2. Calculate `last_idx`
3. Instantiate `grid` to an empty string
4. Iterate over a range from 0 up to input
5.   Print `num` asterisks and continue if `middle`
6.   Calculate `is_before_middle`, less than?
7.   Calculate `distance_from_middle`
8.     If `is_before_middle`, `middle - row`, else `row - middle`
9.   Calculate `leading_spaces`
0.     If `is_before_middle`, `row`, else `last_idx - row`
1.   Print `leading_spaces`, `print_space_separated_stars`
2. Return grid

`print_space_separated_stars`
1. Star, n x spaces, star, n x spaces

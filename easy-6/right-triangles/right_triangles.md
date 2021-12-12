# Right Triangles

## Problem

Write a function that takes a positive integer, n, as an argument, and displays a right triangle whose sides each have n stars. The hypotenuse of the triangle (the diagonal side in the images below) should have one end at the lower-left of the triangle, and the other end at the upper-right.

### Understanding

Input
- Positive integer `n`
Output
- String (stdOut)
  - Right Triangle
    - Stars (`*`)
    - Sides
      - Length of input `n`
      - Right side
        - all Stars
      - Left side
        - One star at bottom
        - Rest spaces
    - Lines
      - First line
        - top
        - `n` - 1 spaces
        - 1 star

## Examples / Test Cases

```python
triangle(5)

#     *
#    **
#   ***
#  ****
# *****

triangle(9)

#         *
#        **
#       ***
#      ****
#     *****
#    ******
#   *******
#  ********
# *********

n = 9
line = 1
stars = 1
spaces = 8 # 9 - 1
```

## Date Structures

- N / A

## Algorithm
Functional Abstractions
- Iteration

1. Set variables for `line` and `stars` to `1`
2. Iterate over range from 1 to `line` to `n` plus 1
  - Calculate `spaces` (`n - line`)
  - Set `stars` to `line`
  - Print spaces then stars

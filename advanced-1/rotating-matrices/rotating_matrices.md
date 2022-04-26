# Rotating Matrices

## Problem

Write a function that takes an arbitrary matrix and rotates it 90 degrees as shown above.

### Understanding

A matrix can be represented in python by a List of Lists.

A 90-degree rotation of a matrix produces a new matrix in which each side of the matrix is rotated clockwise by 90 degrees.

A 90 degree rotation of a non-square matrix is similar.

In action
- Last row becomes the first column
- First row becomes the last column
- And everything in between

In other words
- Create first row from zero indexes in reverse

## Examples / Test Cases

```python
# 1  5  8
# 4  7  2
# 3  9  6

matrix = [
  [1, 5, 8],
  [4, 7, 2],
  [3, 9, 6]
]

'''
Rotated from abobe
3  4  1
9  7  5
6  2  8

Non-square matrix:
3  4  1
9  7  5

becomes:
9  3
7  4
5  1
'''

matrix1 = [
  [1, 5, 8],
# 
  [4, 7, 2],
  [3, 9, 6],
]

matrix2 = [
  [3, 7, 4, 2],
  [5, 1, 0, 8]
]
#           ^

new_matrix2 = [
  [5, 3],
  [1, 7],
  [0, 4],
  [8, 2],
]

row_total = len(matrix2) #=> 2
column_total = 4
column = 3
current_row = 

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]]
new_matrix2 == [
  [5, 3],
  [1, 7],
  [0, 4],
  [8, 2],
]
new_matrix3 == matrix2
```

## Data Structures

- List

## Algorithm
### Functional Abstractions
Reduce
Map

1. Calculate `row_total`, length of input matrix
2. Calculate `column_total`, length of first row
2. Instantiate `new_matrix` List
3. Iterate a range from zero to `column_total` with index as `column`
4.   Instantiate a `new_row` List
5.   Reverse iterate matrix
6.     Access element at `column`
7.     Append current element to `new_row`
8.   Append `new_row` to `new_matrix`
9. Return `new_matrix`

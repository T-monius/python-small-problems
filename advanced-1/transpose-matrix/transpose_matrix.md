# Transpose 3x3

## Problem

Write a function that takes a 3 x 3 matrix in List of Lists format and returns the transpose of the original matrix.

Note that there is a List transpose function that does this -- you may not use it for this exercise. You also are not allowed to a Matrix library. Your task is to do this yourself.

Take care not to modify the original matrix: you must produce a new matrix and leave the original matrix unchanged.

### Understanding

Input
- Matrix
	- List of Lists
- Output
	- Transposition of input
	- Columns => rows

A 3 x 3 matrix can be represented by an List of Lists in which the main List and all of the sub-Lists has 3 elements.

## Examples / Test Cases

```python
matrix = [
  [1, 5, 8],
  [4, 7, 2],
  [3, 9, 6]
]
# ^

idx = 2
new_matrix =[
	[1, 4, 3],
	[5, 7, 9],
	[8, 2, 6]
]

current_row = None

'''
Column = elements of all rows with same index
'''

matrix = [
  [1, 5, 8],
  [4, 7, 2],
  [3, 9, 6]
]

new_matrix = transpose(matrix)

new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]
matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]]
```


```python
1  5  8
4  7  2
3  9  6
```

...can be described by the List of Lists:

```python
matrix = [
  [1, 5, 8],
  [4, 7, 2],
  [3, 9, 6]
]
```

The transpose of a 3 x 3 matrix is the matrix that results from exchanging the columns and rows of the original matrix. For example, the transposition of the List shown above is:

```python
1  4  3
5  7  9
8  2  6
```

## Data Structures

- List

## Algorithm

Functional Abstractions
- MapReduce

__Quadratic solution__
Iterate a range from zero to max index 								 (Reduce)	
	Iterate rows accessing index, pushing to a new array (Map)

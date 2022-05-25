# Merge Sort

## Problem

Sort a list of passed in values using merge sort. You can assume that this list may contain only one type of data. And that data may be either all numbers or all strings.

Merge sort is a recursive sorting algorithm that works by breaking down the list elements into nested sub-lists, then recombining those nested sub-lists in sorted order. It is best shown by example. For instance, let's merge sort the list `[9,5,7,1]`. Breaking this down into nested sub-arrays, we get:

```python
[9, 5, 7, 1] # ->
[[9, 5], [7, 1]] # ->
[[[9], [5]], [[7], [1]]]

'''
We then work our way back to a flat array by merging each pair of nested sub-arrays:
'''
[[[9], [5]], [[7], [1]]] #->
[[5, 9], [1, 7]] #->
[1, 5, 7, 9]
```

### Understanding

Input
- A list
	- Elements
    - Same data type
	   - Important for comparison
    - Numbers
    - Or, Strings

Merge sort
  - Recursive sorting algorithm
  - Breaks down list elements into nested sub-lists
  - Combine sub-lists in sorted order

## Examples / Test Cases

```python
merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9]
merge_sort([5, 3]) == [3, 5]
merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7]

names = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel', 'Kim', 'Bonnie']
sorted_names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue', 'Tyler']
merge_sort(names) == sorted_names

numbers = [
    7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54, 43, 5, 25, 35, 18, 46
]
sorted_numbers = [
    1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25, 35, 37, 43, 46, 51, 54
]
merge_sort(numbers) == sorted_numbers

vals = [9, 5, 7, 1]
[9, 5, 7, 1] # ->
[9, 5] and [7, 1] # -> 
[[9] and [5]] and [[7] and [1]] # returns [5, 9] and [1, 7] respectively
```

## Data Structures

- List

## Algorithm

Base condition
- A single element list
  - Return the list

Perform?
- Split list in half
  - Get length of the list
  - Split length in half and get the integer value
  - Create two lists
    - One up to the middle index
    - One from middle index to length
- Recursively call `merge_sort` on two halves

Combine
- `merge`

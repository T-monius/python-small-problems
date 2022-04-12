# Bubble Sort

## Problem

Bubble Sort is one of the simplest sorting algorithms available. It isn't an efficient algorithm, but it's a great exercise for student developers. In this exercise, you will write a method that does a bubble sort of a List.

A bubble sort works by making multiple passes (iterations) through the List. On each pass, each pair of consecutive elements is compared. If the first of the two elements is greater than the second, then the two elements are swapped. This process is repeated until a complete pass is made without performing any swaps; at that point, the List is completely sorted.

Write a function that takes an List as an argument, and sorts that List using the bubble sort algorithm as just described.

- Note that your sort will be "in-place"; that is, you will mutate the List passed as an argument (Not sure if it can be done in Python). You may assume that the List contains at least 2 elements. 

### Understanding

Input
- List
Output
- List
	- Sorted elements


1. Iterate over list
2.   If first of consecutive elements is greater, swap
When no swaps are performed, stop iterating

## Examples / Test Cases

```python
example_list = [3, 5]
#  							^
# 								 ^
val = 3
next_value = 5

passes = 2
swaps = 0

bubble_sort_bang(example_list)
example_list == [3, 5]

passes = 0
swaps = 0
example_list = [2, 6, 1, 4, 7]
bubble_sort_bang(example_list)
example_list == [1, 2, 4, 6, 7]

example_list = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel', 'Kim', 'Bonnie']
bubble_sort_bang(example_list)
example_list == ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue', 'Tyler']
```

## Data Structures

- List

## Algorithm
### Functional Abstractions
- Iteration
1. Declare `passes` and `swaps` variables setting to `0`
2. While `passes` is less than `1` or `swaps` is greater than `0`
     set swaps to `0`
3.   Iterate over an enumerated list
4.     if `next_val` exists and `val` is greater than `next_val`
5.       increment `swaps`
6.       swap values
7.   Increment `passes`
8. Return the list

# Running Totals

## Problem

Write a method that takes an Array of numbers, and returns an Array with the same number of elements, and each element has the running total from the original Array.

### Understanding

Input
- Array
  - Integer elements
Output
- Array
  - Integer elements
  - Correspond to positional total from previous array

## Examples / Test Cases

```python
running_total([2, 5, 13]) == [2, 7, 20]
running_total([14, 11, 7, 15, 20]) == [14, 25, 32, 47, 67]
running_total([3]) == [3]
running_total([]) == []
```

## Data Structures

- Array

## Algorithm
### Functional Abstractions
- Map / Reduce

### Two easy options
1. Iterate with a total and push to a return array at every index
2. Iterate with and index and sum a silice for index, inclusive

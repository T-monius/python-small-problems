# Sum of Sums

## Problem

Write a function that takes an List of numbers and then returns the sum of the sums of each leading subsequence for that List. You may assume that the List always contains at least one number.

### Understanding

Input
- List
  - Number elements
Output
- Number
  - Sum of all slices from the list

## Examples / Test Cases

```python
sum_of_sums([3, 5, 2]) == (3) + (3 + 5) + (3 + 5 + 2) # -> (21)
sum_of_sums([1, 5, 7, 3]) == (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) # -> (36)
sum_of_sums([4]) == 4
sum_of_sums([1, 2, 3, 4, 5]) == 35

'''
[3, 5, 2]
       ^

idx = 2
slices = [[3], [3, 5], [3, 5, 2]] # Transform
sums = [3, 8, 10]                 # Transform
sum = 21                          # Reduce
'''
```

## Data Structures

- List

## Algorithm
Functional Abstractions
- Transformation
- Reduction

1. Declare a starting `idx` setting to `1`
2. Declare a `slices` list
3. Iterate input list
  - pushing slices up to current `idx` to `slices`
4. Map `slices`
  - Sum at every slice
5. Sum result of previous mapping and Return

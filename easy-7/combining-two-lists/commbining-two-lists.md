# Combinging Two Lists

## Problem

Write a function that combines two Lists passed in as arguments, and returns a new List that contains all elements from both List arguments, with the elements taken in alternation.

You may assume that both input Lists are non-empty, and that they have the same number of elements.

### Understanding

Input
- Two arguments
  - Both lists
  - Arbitrary elements
  - Same length
  - Non-empty
Output
- Single list
  - Interleaved elements of first two
    - Alternate
    - Starts w/ first element of first input list

Using `for` I don't necessarily have an `idx`
- Can use for to iterate over one array, then an `idx` to reference secondary

## Examples / Test Cases

```python
interleave([1, 2, 3], ['a', 'b', 'c']) == [1, 'a', 2, 'b', 3, 'c']
interleave([], []) == []

# [1, 2, 3]
#        ^
# ['a', 'b', 'c']
#             ^

idx = 2

interleaved = [1, 'a', 2, 'b', 3, 'c']
```

## Data Structures

- N / A

## Algorithm
Functional Abstractions
- Transformation?
- Iteration

1. Declare an `idx` and set to `0`
2. Declare a list for return
3. For each element of `primary_list`
  - Append element at iteration to new list
  - Access element of secondary list
    - Append to new list
  - Increment `idx`
4. Return new list

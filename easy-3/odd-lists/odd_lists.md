# Odd Lists

## Problem

Write a method that returns an Array that contains every other element of an Array that is passed in as an argument. The values in the returned list should be those values that are in the 1st, 3rd, 5th, and so on elements of the argument Array.

### Understanding

Input
- Array
  - Arbitrary element data types
Output
- Array
  - Alternating subset of input elements
  - Even indexed

## Examples / Test Cases

```python
oddities([2, 3, 4, 5, 6]) == [2, 4, 6]
oddities(['abc', 'def']) == ['abc']
oddities([123]) == [123]
oddities([])  == []
other_oddities([2, 3, 4, 5, 6])  == [2, 4, 6]
other_oddities(['abc', 'def']) == ['abc']
other_oddities([123])  == [123]
other_oddities([])  == []
```

## Data Structures

- List

## Algorithm
### Functional Abstractions
- Selection

### Hard Algortithm

- Set an index variable to zero
- Declare a variable for even indexed values
- Iterate over input array
  - Select values even indexed values
- Return

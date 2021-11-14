# Multiples of Three and Five

## Problem

Write a method that searches for all multiples of 3 or 5 that lie between 1 and some other number, and then computes the sum of those multiples. For instance, if the supplied number is 20, the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

You may assume that the number passed in is an integer greater than 1.

### Understanding

Input
- Integer
Output
- Integer
  - Represents all multiples of 3 and 5 between 1 and input number summed

## Examples / Test Cases

```python
multisum(3) == 3
multisum(5) == 8
multisum(10) == 33
multisum(1000) == 234168
```

## Data Structures

- Range
- Array

## Algorithm
### Functional Abstractions
- Selection
- Reduction

### Hard Algorithm

- Instantiate a `multiples` variable to an array
- Select multiples of 3 and five from a range
- Reduce array / summing

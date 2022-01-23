# Uppercase Check

## Problem

Write a function that takes a string argument, and returns `true` if all of the alphabetic characters inside the string are uppercase, `false` otherwise. Characters that are not alphabetic should be ignored

### Understanding

Input
- Single Argument
  - String
Output
- boolean
  - Determine if all of alpha characters are uppercase


## Examples / Test Cases

```python
is_uppercase('t') == False
is_uppercase('T') == True
is_uppercase('Four Score') == False
is_uppercase('FOUR SCORE') == True
is_uppercase('4SCORE!') == True
is_uppercase('') == True
```

## Data Structures

- N / A

## Algorithm

1. Iterate over the input string
  - If character at iteration is alpha
    - return `False` if the character is not equal to itself
      when `upper` is invoked on it.
2. Return `True`

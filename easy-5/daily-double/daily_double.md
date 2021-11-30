# Daily Double

## Problem

Write a function that takes a string argument and returns a new string that contains the value of the original string with all consecutive duplicate characters collapsed into a single character.

### Understanding

Input
- String
Output
- No cosecutive duplicate characters

## Examples / Test Cases

```python
crunch('ddaaiillyy ddoouubbllee') == 'daily double'
crunch('4444abcabccba') == '4abcabcba'
crunch('ggggggggggggggg') == 'g'
crunch('a') == 'a'
crunch('') == ''

str = 'ddaaiillyy ddoouubbllee'
                  ^

collapsed_str = 'daily d'
```

## Data Structures

- Sting

## Algorithm
- Iteration
### Hard Algorithm
1. Declare new return sting `collapsed_str`
2. Iterate over inptut string
  - Conditionally push current char
    - if `collapsed` is empty
    - OR, Compare current char to `collapsed_str[-1]` is equal
3. Return `collapsed_str`


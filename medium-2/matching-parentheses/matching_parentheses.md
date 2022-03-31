# Matching Parentheses?

## Problem

Write a function that takes a string as an argument, and returns `True` if all parentheses in the string are properly balanced, `False` otherwise. To be properly balanced, parentheses must occur in matching `'('` and `')'` pairs.

### Understanding

Input
- String
	- Determine if all parentheses properly open and close
Output
- Boolean

A closing parentheses cannot precede
- Keep count
  - If closing count is greater then open, unbalanced
  - If count not even after iteration, unbalanced

## Examples / Test Cases

```python
is_balanced('What (is) this?') == True
is_balanced('What is) this?') == False
is_balanced('What (is this?') == False
is_balanced('((What) (is this))?') == True
is_balanced('((What)) (is this))?') == False
is_balanced('Hey!') == True
is_balanced(')Hey!(') == False
is_balanced('What ((is))) up(') == False

text = '((What)) (is this))?'
#                         ^

open_count = 3
close_count = 4
```

## Data Structures

- N/A

## Algorithm

1. Instantiate count variables, setting to `0`
2. Iterate over the input text
3.   Return `False` if the `closed_count` is greater than `open_count`
4.   If the `current_char` is open or closed paren, increment
5. Return `True` if the count is equal
6. Return `False`

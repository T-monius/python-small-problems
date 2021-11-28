# Clean up the Words

## Problem

Given a string that consists of some words (all lowercased) and an assortment of non-alphabetic characters, write a method that returns that string with all of the non-alphabetic characters replaced by spaces. If one or more non-alphabetic characters occur in a row, you should only have one space in the result (the result should never have consecutive spaces).

### Understanding

Input
- String
  - Words
    - All lowercase
    - Non-alphas
Output
- String
  - Non-alphas replaced by spaces
  - Consecutive non-alphas replaced by a single-space

`String#tr_s` would handle this in Ruby
`String.protoptype.replace` in JS or Ruby `String#gsub` could handle

Can handle this with simple iteration

```python
cleanup("---what's my +*& line?") == ' what s my line '

'''Playground'''
"---what's my +*& line?"
^
```

## Data Structures

- str

## Algorithm

Iterate over string
- If character at iteration is alpha, push it to a list
- Else
  - Pushs a space if the last character of the array isn't a space
### Functional Abstractions
- Iteration
  - Selection

### Hard Algorithm

- Declare an str for 'non-alphas'
- Iterate over input string
  - Conditionally push character at iteration to return array
  - Else
    - Conditionally push space
- Return non-alphas str

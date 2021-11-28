# Letter Conter

## Problem

Write a function that takes a string with one or more space separated words and returns a dict that shows the number of words of different sizes.

Words consist of any string of characters that do not include a space.

### Understanding

Input
- String
  - One or more space separated words
    - Words = consecutive `\S` characters
Output
- Dictionary
  - Counts
  - Words of different lengths

## Examples / Test Cases

```python
word_sizes('Four score and seven.') == { 3: 1, 4: 1, 5: 1, 6: 1 }
word_sizes('Hey diddle diddle, the cat and the fiddle!') == { 3: 5, 6: 1, 7: 2 }
word_sizes("What's up doc?") == { 6: 1, 2: 1, 4: 1 }
word_sizes('') == {}
```

## Data Structures

- Dictionary

## Algorithm
### Functional Abstractions
- Reduce

### Hard Algorithm
- Declare a return `occurrences` dictionary
- Split input string
- Iterate over words
  - If length of the word at iteration is in `occurrences`
    - Increment it
  - Else
    - Assign it the value of 1
- Return `occurrences`

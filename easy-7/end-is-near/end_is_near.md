# The End Is Near But Not Here

## Problem

Write a function that returns the penultimate word in the String passed to it as an argument.

Words are any sequence of non-blank characters.

You may assume that the input String will always contain at least two words.

### Understanding

Input
- String
	- Non-empty
	- Words
		- At least two separate sequences non-whitespace characters
Output
- String
	- Word
		- series of characters
		- `\S`

## Examples / Test Cases

```python
penultimate('last word') == 'last'
penultimate('Launch School is great!') == 'is'

'''
'last word'

words = ['last', 'word']
 					^

words[-2:-1]
'''
```

## Data Structures

- List

## Algorithm
Functional Abstractions

1. Split the string
2. Access the second to the last word
3. Return

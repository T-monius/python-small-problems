# Capitalize Words

## Problem

Write a function that takes a single String argument and returns a new string that contains the original value of the argument with the first character of every word capitalized and all other letters lowercase.

You may assume that words are any sequence of non-blank characters.

### Understanding

Python as an `title`

Input
- Single string
	- words
		- Space separated series of alpha characters
	- Special characters
		- Quotes
Output
- Capitalize all words in input string

## Examples / Test Cases

```python
word_cap('four score and seven') == 'Four Score And Seven'
word_cap('the javaScript language') == 'The Javascript Language'
word_cap('this is a "quoted" word') == 'This Is A "quoted" Word'

phrase = 'this is a "quoted" word'

words = ['this', 'is', 'a', '"quoted"', 'word']
#                      					^ 

word = '"quoted"'
```

## Data Structures

- List

## Algorithm
Functional Abstraction
- Transformation (map)

1. Split the phrase by space
2. Iterate each word (list comprehension)
	- Ternary
		- Title case a word of first char is alpha
3. Join with a space and return

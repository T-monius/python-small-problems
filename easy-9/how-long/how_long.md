# How Long Are You?

## Problem

Write a function that takes a string as an argument and returns a List that contains every word from the string to which you have appended a space and the word length.

You may assume that words in the string are separated by exactly one space, and that any substring of non-space characters is a word.

### Understanding

Input
- String
Output
- List
	- Words
		- Appended:
			- Space
			- Word length

Words are separated by a single space
All substrings are words

## Examples / Test Cases

```python
word_lengths("cow sheep chicken") == ["cow 3", "sheep 5", "chicken 7"]

word_lengths("baseball hot dogs and apple pie") ==
  ["baseball 8", "hot 3", "dogs 4", "and 3", "apple 5", "pie 3"]

word_lengths("It ain't easy, is it?") == ["It 2", "ain't 5", "easy, 5", "is 2", "it? 3"]

word_lengths("Supercalifragilisticexpialidocious") ==
  ["Supercalifragilisticexpialidocious 34"]

word_lengths("") == []
```

## Data Structures

- List

## Algorithm

Functional Abstractions
- Transformation

1. Split `src` string
2. `map` list of words (can use a list comprehension)
	- Append space and length of word at iteration
3. Return mapped list

# Word to Digit

## Problem

Write a function that takes a sentence string as input, and returns the same string with any sequence of the words 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' converted to a string of digits.

### Understanding

Input
- String
	- Sentence, space separated words
Output
- String
	- Replace occurrences of words describing numbers with numeric digits characters

## Examples / Test Cases

```python
word_to_digit('Please call me at five five five one two three four. Thanks.') == 'Please call me at 5 5 5 1 2 3 4. Thanks.'

word_numbers = ['zero', 'one', 'two', 'three', 'four', 'five',
							 #  				^
							  'six', 'seven','eight', 'nine']

word_digit_dict = { 'zero': 0, 'one': 1, 'two': 2, 'three': 3,
									  'four':4, 'five': 5, 'six': 6, 'seven': 7,
									  'eight': 8, 'nine': 9 }

sentence = 'Please call me at five five five 1 two three four. Thanks.'
# ['Please', 'call', 'me', 'at', 'five', 'five',
# 'five', 'one', 'two', 'three', 'four.', 'Thanks.']
#  																	^

# 'four.' => word, punctuation

current_word
new_sentence = ['Please', 'call', 'me', 'at', '5', '5', '5', '1', '2', '3', ]
```

## Data Structures

- Dictionary
- List

## Algorithm

- Create `word_digit_dict`
- Split input sentence
- Map words
	- `word_to_digit_mapper`
		- Conditionally store punctuation else `''`
		- If `word` is in the dict
			- Replace it
		- Else
			- The word itself
		- Attach and return `word` with `punctuation`
- Join words

# Reverse It

## Problem 1

Write a method that takes one argument, a string, and returns a new string with the words in reverse order.

### Understanding

Input
- String
	- Space separated words
	- And, otherwise
Output
- String
	- Input words in reverse

## Data Structures

List

## Algorithm

1. Split the input string
2. Reverse array
3. Join array
4. Return

## Problem 2

Write a method that takes one argument, a string containing one or more words, and returns the given string with words that contain five or more characters reversed. Each string will consist of only letters and spaces. Spaces should be included only when more than one word is present.

### Understanding

Input
- One string
	- One or more words, phrase
Output
- String
	- Conditionally reversed words
		- Words longer than 5 char reversed
Python's `reverse` method only operates on Lists
- Mutating


## Examples / Test Cases

'Professional'           -> lanoisseforP
'Walk around the block'  -> Walk dnuora the kcolb
'Launch School' 				 -> hcnuaL loohcS

## Data Structures

Array

1. Split the input string
2. Iterate over the words
	- Conditionally Reverse them
		- Helper method reverse_word
3. Join array
4. Return

Helper method
1. Declare a return string
2. Iterate the string backwards
	1. Concatenate char at iteration to the return string
3. Return the reversed word

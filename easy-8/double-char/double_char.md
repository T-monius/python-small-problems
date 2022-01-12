# Double Char

## Problem 1

Write a function that takes a string and returns a new string in which every character is doubled.

### Understanding

Input
- String
Output
- New string
	- Every character of input string doubled
	- Twice the length of input?
		- Do space and special characters count?

## Examples / Test Cases

```python
repeater('Hello') == 'HHeelllloo'
repeater('Good job!') == 'GGoooodd  jjoobb!!'
repeater('') == ''

new_str = []
sample = 'Hello'
#          ^
```

## Data Structures

- List

## Algorithm
Functional Abstraction
- Reduce?
- Map
1. Declare a new list
2. Iterate over the characters of the input string
3. For each character, double it and append to the list OR push 2 to the list
4. Join the elements of the list and return

## Problem 2

Write a function that takes a string and returns a new string in which every consonant character is doubled. Vowels (a, e, i, o, u), digits, punctuation, and whitespace should not be doubled

### Understanding

Similar to previous, but interrogate characters before doubling
- Case insensitive

## Examples / Test Cases

```python
double_consonants('String') == 'SSttrrinngg'
double_consonants('Hello-World!') == 'HHellllo-WWorrlldd!'
double_consonants('July 4th') == 'JJullyy 4tthh'
double_consonants('') == ''
```

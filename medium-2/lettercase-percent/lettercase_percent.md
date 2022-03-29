# Lettercase Percentage Ratio

## Problem

In the easy exercises, we worked on a problem where we had to count the number of uppercase and lowercase characters, as well as characters that were neither of those two. Now we want to go one step further.

Write a function that takes a string, and then returns a dictionary that contains 3 entries: one represents the percentage of characters in the string that are lowercase letters, one the percentage of characters that are uppercase letters, and one the percentage of characters that are neither.

You may assume that the string will always contain at least one character.

### Understanding

Input
- String
	- Alphanum
	- Non-alpha
	- Whitespace
Output
- Dictionary
	- 3 keys
		1. uppercase percentage
		2. lowercase percentage
		3. neither percentage

### Examples / Test Cases

```python
letter_percentages('abCdef 123') == { 'lowercase': 50.0, 'uppercase': 10.0, 'neither': 40.0 }
letter_percentages('AbCd +Ef') == { 'lowercase': 37.5, 'uppercase': 37.5, 'neither': 25.0 }
letter_percentages('123') == { 'lowercase': 0.0, 'uppercase': 0.0, 'neither': 100.0 }

'''
'abCdef 123'
          ^
lower_count = 4 => pecent = 
uppercount = 2
neither_count = 4

percent algorithm: (wp / 100) x len = target
- 'target' will be one of the counts
- Cross multiply and divide
	- (target * 100) / len
	- i.e. (4 * 100) / 10 => 400 / 10 => 40%
'''
```

## Data Structures

- Dict

## Algorithm

1. Instantiate `percentages` dictionary
1. Instantiate 3 count variables
1. Iterate over input string
1.   Increment appropriate counter
1. For each count type
1.   Calculate value
1.   Assign to dictionary key
1. Return dictionary

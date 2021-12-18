# Staggered Caps

## Problem

Write a function that takes a String as an argument, and returns a new String that contains the original value using a staggered capitalization scheme in which every other character is capitalized, and the remaining characters are lowercase. Characters that are not letters should not be changed, but count as characters when switching between upper and lowercase.

### Understanding

Input
- Single string
	- Arbitrary characters
	- To include alpha
Output
-	Single string
	- Staggered upper case letters
		- Every other index is upper case

## Example / Test Cases

```python
staggered_case('I Love Launch School!') == 'I LoVe lAuNcH ScHoOl!'
staggered_case('ALL_CAPS') == 'AlL_CaPs'
staggered_case('ignore 77 the 444 numbers') == 'IgNoRe 77 ThE 444 NuMbErS'

normal_case = 'I Love Launch School!'
# 						        ^
'''
Even indexes are capitalized

params = normal_case, staggered='I LoVe l'

idx = len(staggered)          # 7
if idx == len(normal_case)
	return staggered

Access current_char from normal_case

if idx % 2 == 0:
    Replace current_char with uppercase
else:
	  lowercase current_char

return recursive call to staggered_case
'''
```

## Data Structures

- N/A

## Algorithm
Functional Abstractions
- Iteration

1. Evaluate base case
	- Return string being length of input string
	- Conditionally return return string
2. Access current char from length of return string
3. Conditionally uppercase current char
4. Recursively call function

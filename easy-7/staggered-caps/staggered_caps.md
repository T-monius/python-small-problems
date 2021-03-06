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

## Problem 2

Modify the function from the previous exercise so it ignores non-alphabetic characters when determining whether it should uppercase or lowercase each letter. The non-alphabetic characters should still be included in the return value; they just don't count when toggling the desired case.

### Understanding

Input
- String
	- Arbitrary characters
	- Include alphas
Output
- String where every other alpha character is capitalized

Capitalized every odd count alpha.
- The first is capitalized

## Examples / Test Cases

```python
alpha_staggered_case('I Love Launch School!') == 'I lOvE lAuNcH sChOoL!'
alpha_staggered_case('ALL CAPS') == 'AlL cApS'
alpha_staggered_case('ignore 77 the 444 numbers') == 'IgNoRe 77 ThE 444 nUmBeRs'

'''
'I Love Launch School!'
   ^

idx = 3
char = 'L'
alpha_count = 2
str = 'I l'
'''
```



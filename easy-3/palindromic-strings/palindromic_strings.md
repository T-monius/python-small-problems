# Palindromic Striongs

## Problem 1

Write a method that returns true if the string passed as an argument is a palindrome, false otherwise. A palindrome reads the same forward and backward. For this exercise, case matters as does punctuation and spaces.

### Understanding

Input
- String
Output
- Boolean
	- Determine whether input string is a palindrome

Palindromes are the same forward and backward
- Case matters
- Punctuation and spaces matter

## Examples / Test Cases

```python
is_palindrome('madam') == True
is_palindrome('Madam') == False          # (case matters)
is_palindrome("madam i'm adam") == False # (all characters matter)
is_palindrome('356653') == True

'''
'madam'
  ^
    ^
While left poiter is less than right
	- Comnpare characters at indexes
'''
```

## Data Structures

- N/A

## Algorithm
### Functional Abstractions
- Interrogatoion

### Steps

1. Declare to pointers
	- Start
	- End
2. Iterate while the start pointer is less than the end
3. Access characters
4. If characters are not equal, return `False`
5. Increment start
6. Decrement end
7. Return `True`

## Problem 2

Write another method that returns true if the string passed as an argument is a palindrome, false otherwise. This time, however, your method should be case-insensitive, and it should ignore all non-alphanumeric characters. If you wish, you may simplify things by calling the palindrome? method you wrote in the previous exercise.

## Understanding

Don't respect case
Only check alphas

## Examples / Test Cases

```python
is_real_palindrome('madam') == True
is_real_palindrome('Madam') == True           # (case does not matter)
is_real_palindrome("Madam, I'm Adam") == True # (only alphanumerics matter)
is_real_palindrome('356653') == True
is_real_palindrome('356a653') == True
is_real_palindrome('123ab321') == False
```

## Algorithm
- Same as before, but add `continue` for non-alphas

## Problem 3

Palindromic Numbers

- Write a method that returns true if its integer argument is palindromic, false otherwise. A palindromic number reads the same forwards and backwards.

### Understanding

Need to access digits of number.
Either convert it to a string or list

## Examples / Test Cases

```python
is_palindromic_number(34543) == True
is_palindromic_number(123210) == False
is_palindromic_number(22) == True
is_palindromic_number(5) == True
```

## Data Structures

- N/A

## Algorithm

- Convert input to a string.
- Call one of the previous palindome methods on it

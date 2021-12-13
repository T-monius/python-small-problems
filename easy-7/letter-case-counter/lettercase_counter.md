# Lettercase Counter

## Problem

Write a function that takes a string, and then returns a dictionary that contains 3 entries: one represents the number of characters in the string that are lowercase letters, one the number of characters that are uppercase letters, and one the number of characters that are neither.

### Understanding

Function
Input
- String
Outpu
- Dictionary
  - 3 Entries
    - Upper count
    - Lower count
    - Neither count

## Examples / Test Cases

```python
letter_case_count('abCdef 123') == { lowercase: 5, uppercase: 1, neither: 4 }
letter_case_count('AbCd +Ef') == { lowercase: 3, uppercase: 3, neither: 2 }
letter_case_count('123') == { lowercase: 0, uppercase: 0, neither: 3 }
letter_case_count('') == { lowercase: 0, uppercase: 0, neither: 0 }

'''
'abCdef 123'
          ^

lwer = 5
upper = 1
neither = 4
'''
```

## Data Structures

- N / A

## Algorithm
Functional Abstractions
- Iteration

1. `import re`
2. Declare a count / seen dictionary
  - Set three entries to zero?
3. Loop over the string w/ `for`
  - If the char at iteration is lower (test with regex)
    - Increment lower count
  - Same for upper and neitehr
4. return dictionary

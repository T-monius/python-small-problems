# Letter Swap

## Problem

Given a string of words separated by spaces, write a function that takes this string of words and returns a string in which the first and last letters of every word are swapped.

You may assume that every word contains at least one letter, and that the string will always contain at least one word. You may also assume that each string contains nothing but words and spaces

### Understanding

Input
- String
  - Represent words
Output
- String
  - First and last letters of words swapped

Every word contains at least 1 letter
String will contain at least 1 word
Each string contains only words and spaces

Ruby's parallel assignment allows swapping. Not sure if Python's allows for that.

## Examples / Test Cases

```ruby
word = 'hello'

word[0], word[-1] = word[-1], word[0]
#=> 'oellh'
```

```python
swap('Oh what a wonderful day it is') == 'hO thaw a londerfuw yad ti si'
swap('Abcde') == 'ebcdA'
swap('a') == 'a'
```

## Data Structures

- N/A

## Algorithm
### Functional Abstractions
- Transformation

### Hard Algorithm
1. Split the string by whitespace
2. Map
3. For each word
  - If one letter
    - return
  - If two letters
    - swap
  - If three >
    - assign `first`, `middle`, `last` variables
    - return `last`, `middle`, `first`
4. Join the list

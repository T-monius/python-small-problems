# Group Anagrams

## Problem

Given the list:

```python
words =  ['demo', 'none', 'tied', 'evil', 'dome', 'mode', 'live',
          'fowl', 'veil', 'wolf', 'diet', 'vile', 'edit', 'tide',
          'flow', 'neon']
```

Write a program that prints out groups of words that are anagrams. Anagrams are words that have the same exact letters in them but in a different order. Your output should look something like this:

```python
["demo", "dome", "mode"]
["neon", "none"]
#(etc)
```

### Understanding

Must determine which words are anagrams of other words in the list.
Filter the list for anagrams of a given word.
Must remove a group from the list each time one is found; otherwise, create multiple duplicate groups and dedup them.

## Examples / Test Cases

```python
words =  ['demo', 'none', 'tied', 'evil', 'dome', 'mode', 'live',
					# 				w
          'fowl', 'veil', 'wolf', 'diet', 'vile', 'edit', 'tide',

          'flow', 'neon']
					#        ^

idx = 1
secondary_idx = 15
seen_anagrams = { 0:True, 4:True, 5:True, 1:True, 15:True }
all_anagrams = [['demo', 'dome', 'mode']]
anagrams = ['none', 'neon']
word = 'none'

```

## Data Structures

- List
- Dictionary

## Algorithm

1. Declare an `all_anagrams` variable setting it to an empty list
2. Declare an empty `seen_anagrams` dict
3. Iterate over the input list with indexes
4.   If the index `i` is in `seen_anagrams`, `pass`
     Assign `sorted_word_chars` to a sorted list of chars in current word
     Assign `anagrams` to an empty list
5.   Else iterate over the list again with indexes
6. 	   If the current index `j` is equal to `i`, `pass`
7.     If `j` is in `seen_anagrams`, `pass`
8.     If `word_chars` and the sorted secondary word chars are equal
9.       Append secondary word to `anagrams`
10.      Add secondary to `seen_anagrams`
11.  If `anagrams` is not empty
       Append current word to it
       Add `anagrams` to `all_anagrams`
12. Return `all_anagrams`

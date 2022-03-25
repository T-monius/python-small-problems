# Now I Know My ABCs

## Problem

A collection of spelling blocks has two letters per block, as shown in this list:

```
N:A   B:O   C:P   D:Q   R:E   F:S

G:T   H:U   V:I   J:W   X:K   L:Y

Z:M
```

This limits the words you can spell with the blocks to just those words that do not use both letters from any given block. Each block can only be used once.

Write a functions that returns `True` if the word passed in as an argument can be spelled from this set of blocks, `False` otherwise.

### Understanding

Input
- String
  - All alpha
  - Case insensitive
- Output
  - Boolean
  - Can word be spelled with blocks

Blocks
- Contain two letters
- Predetermined

## Examples / Test Cases

```python
block_word?('BATCH') == True
block_word?('BUTCH') == False
block_word?('jest') == True

used_letters = {'B', 'O', 'U', 'H', 'T', 'G', 'C', 'P'}
word = 'BUTCH'
#           ^
```

## Data Structures

- Set

## Algorithm

1. Create `BLOCK_LETTER_DICT`
2. Instantiate an empty set `seen_letters`
3. Uppercase the word
3. Iterate over `word`
4.   Retrieve mathcing letter
5.   Return `False` if letter or it's match are in the set
6.   Add letter and its match to `seen_letters`
7. Return `True`

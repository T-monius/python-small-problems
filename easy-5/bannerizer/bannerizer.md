# Bannerizer

## Problem

Write a function that will take a short line of text, and prints it within a box.

### Understanding

Function
Input
- String
	- Short (less than 80 chars?)
Output
- Print a box with text in it

Box height, beginning, and end characters are always the same

### Examples / Test Cases

```python
print_in_box('To boldly go where no one has gone before.')
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

print_in_box('')
# +--+
# |  |
# |  |
# |  |
# +--+

'''
Outer line = '+-{    lines     }-+'
Inner line = '| {spaces OR text} |'
'''
```

## Data Structures

- N/A

## Algorithm
1. Create `inner_line` and `outer_line` functions
	- Print input with given argument
2. Call methods with text length or text
